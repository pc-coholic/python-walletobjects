import base64
import json
import struct
import time
from json import JSONDecodeError

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS


def lazyi18n_to_dict(lazyi18nstring):
    return dict(lazyi18nstring.data)


def localized_string(strings_dict, default=None):
    if not isinstance(strings_dict, dict) and type(strings_dict).__name__ is not 'LazyI18nString':
        raise TypeError('localizedString is not of instance dict or LazyI18nString')

    if type(strings_dict).__name__ is 'LazyI18nString':
        strings_dict = lazyi18n_to_dict(strings_dict)

    localized = {
        'kind': 'walletobjects#localizedString',
    }

    if default in strings_dict:
        default_lang = default
    else:
        default_lang = next(iter(strings_dict))

    localized['defaultValue'] = {
        'kind': 'walletobjects#translatedString',
        'language': default_lang,
        'value': strings_dict[default_lang]
    }
    strings_dict.pop(default_lang)

    translated_values = []
    for key, value in strings_dict.items():
        translated_values.append(
            {
                'kind': 'walletobjects#translatedString',
                'language': key,
                'value': value
            }
        )

    localized['translatedValues'] = translated_values

    return localized


def localized_uri(uri, description, strings_dict, default=None):
    if not isinstance(strings_dict, dict) and type(strings_dict).__name__ is not 'LazyI18nString':
        raise TypeError('localizedString is not of instance dict or LazyI18nString')

    if type(strings_dict).__name__ is 'LazyI18nString':
        strings_dict = lazyi18n_to_dict(strings_dict)

    return {
        'kind': 'walletobjects#uri',
        'uri': uri,
        'description': description,
        'localizedDescription': localized_string(strings_dict, default),
    }


def lat_long_point(latitude, longitude):
    return {
        'kind': 'walletobjects#latLongPoint',
        'latitude': latitude,
        'longitude': longitude,
    }


def image(uri, description, strings_dict, default=None):
    if not isinstance(strings_dict, dict) and type(strings_dict).__name__ is not 'LazyI18nString':
        raise TypeError('localizedString is not of instance dict or LazyI18nString')

    if type(strings_dict).__name__ is 'LazyI18nString':
        strings_dict = lazyi18n_to_dict(strings_dict)

    return {
        'kind': 'walletobjects#image',
        'sourceUri': localized_uri(uri, description, strings_dict, default)
    }


def venue(name, address, default=None):
    if not isinstance(name, dict) and type(name).__name__ is not 'LazyI18nString':
        raise TypeError('name is not of instance dict or LazyI18nString')

    if not isinstance(address, dict) and type(address).__name__ is not 'LazyI18nString':
        raise TypeError('address is not of instance dict or LazyI18nString')

    if type(name).__name__ is 'LazyI18nString':
        name = lazyi18n_to_dict(name)

    if type(address).__name__ is 'LazyI18nString':
        address = lazyi18n_to_dict(address)

    return {
        'kind': 'walletobjects#eventVenue',
        'name': localized_string(name, default),
        'address': localized_string(address, default)
    }


def message(header, localizedHeader, body, localizedBody, default=None):
    return {
        'kind': 'walletobjects#walletObjectMessage',
        'header': header,
        'localizedHeader': localized_string(localizedHeader, default),
        'body': body,
        'localizedBody': localized_string(localizedBody, default),
    }


def pack(string):
    return struct.pack('<Q', len(string))[:4] + bytes(string, 'utf-8')


def unseal_callback(callback_body: dict, issuer_id: str) -> dict:
    if not isinstance(callback_body, dict):
        raise TypeError("callback_body is not a dict or json object")

    if not all(k in callback_body for k in ('signature', 'intermediateSigningKey', 'protocolVersion', 'signedMessage')):
        raise ValueError("callback_body does not contain all vital keys: signature, intermediateSigningKey, protocolVersion, signedMessage")

    r = requests.get("https://pay.google.com/gp/m/issuer/keys")

    try:
        pksjson = json.loads(r.content)
    except JSONDecodeError:
        raise ValueError("Could not verify signature: couldn't download public key")

    if 'keys' not in pksjson:
        raise ValueError("Could not verify signature: no public keys in server response")

    webhook_validated = False
    intermediate_validated = False

    for pkjson in pksjson['keys']:
        if int(pkjson['keyExpiration'])/1000 > int(time.time()):
            try:
                pk = ECC.import_key(base64.b64decode(pkjson['keyValue']))
            except ValueError:
                break

            # Verify Intermediate Signed Key with Public Key
            verifier = DSS.new(pk, 'fips-186-3', 'der')
            for signature in callback_body['intermediateSigningKey']['signatures']:
                try:
                    verifier.verify(
                        SHA256.new(
                            pack('GooglePayPasses') + pack(pkjson['protocolVersion']) +
                            pack(callback_body['intermediateSigningKey']['signedKey'])
                        ),
                        base64.b64decode(signature)
                    )
                    intermediate_validated = True
                    break
                except ValueError:
                    pass

            if intermediate_validated:
                intermediateSigningKey = json.loads(callback_body['intermediateSigningKey']['signedKey'])

                if int(intermediateSigningKey['keyExpiration']) / 1000 > int(time.time()):
                    try:
                        sk = ECC.import_key(base64.b64decode(intermediateSigningKey['keyValue']))
                    except ValueError:
                        break

                # Verify signedMessage with intermediateSigningKey / signedKey
                verifier = DSS.new(sk, 'fips-186-3', 'der')
                try:
                    verifier.verify(
                        SHA256.new(
                            pack('GooglePayPasses') + pack(str(issuer_id)) +
                            pack(callback_body['protocolVersion']) + pack(callback_body['signedMessage'])
                        ),
                        base64.b64decode(callback_body['signature'])
                    )
                    webhook_validated = True
                    break
                except ValueError:
                    pass

    if intermediate_validated and webhook_validated:
        return json.loads(callback_body['signedMessage'])
    else:
        raise ValueError("Could not validate signature")
