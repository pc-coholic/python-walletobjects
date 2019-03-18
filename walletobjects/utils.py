import base64
import json
import struct
import time
from json import JSONDecodeError
from typing import Dict, Optional

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import ECC
from Crypto.Signature import DSS


class utils(object):
    def LazyI18nToDict(LazyI18nString) -> Dict[str, str]:
        return dict(LazyI18nString.data)

    def localizedString(stringsDict: Dict[str, str], default: Optional[str] = None) -> str:
        if not isinstance(stringsDict, dict) and type(stringsDict).__name__ is not 'LazyI18nString':
            raise TypeError('localizedString is not of instance dict or LazyI18nString')

        if type(stringsDict).__name__ is 'LazyI18nString':
            stringsDict = utils.LazyI18nToDict(stringsDict)

        localizedString = {
            'kind': 'walletobjects#localizedString',
        }

        if default in stringsDict:
            defaultLang = default
        else:
            defaultLang = next(iter(stringsDict))

        localizedString['defaultValue'] = {
            'kind': 'walletobjects#translatedString',
            'language': defaultLang,
            'value': stringsDict[defaultLang]
        }
        stringsDict.pop(defaultLang)

        translatedValues = []
        for key, value in stringsDict.items():
            translatedValues.append(
                {
                    'kind': 'walletobjects#translatedString',
                    'language': key,
                    'value': value
                }
            )

        localizedString['translatedValues'] = translatedValues

        return localizedString

    def localizedUri(uri: str, description: str, stringsDict: Dict[str, str], default: Optional[str] = None) -> str:
        if not isinstance(stringsDict, dict) and type(stringsDict).__name__ is not 'LazyI18nString':
            raise TypeError('localizedString is not of instance dict or LazyI18nString')

        if type(stringsDict).__name__ is 'LazyI18nString':
            stringsDict = utils.LazyI18nToDict(stringsDict)

        return {
            'kind': 'walletobjects#uri',
            'uri': uri,
            'description': description,
            'localizedDescription': utils.localizedString(stringsDict, default),
        }

    def latLongPoint(latitude: float, longitude: float) -> str:
        return {
            'kind': 'walletobjects#latLongPoint',
            'latitude': latitude,
            'longitude': longitude,
        }

    def image(uri: str, description: str, stringsDict: Dict[str, str], default: Optional[str] = None) -> str:
        if not isinstance(stringsDict, dict) and type(stringsDict).__name__ is not 'LazyI18nString':
            raise TypeError('localizedString is not of instance dict or LazyI18nString')

        if type(stringsDict).__name__ is 'LazyI18nString':
            stringsDict = utils.LazyI18nToDict(stringsDict)

        return {
            'kind': 'walletobjects#image',
            'sourceUri': utils.localizedUri(uri, description, stringsDict, default)
        }

    def venue(name: Dict[str, str], address: Dict[str, str], default: Optional[str] = None) -> str:
        if not isinstance(name, dict) and type(name).__name__ is not 'LazyI18nString':
            raise TypeError('name is not of instance dict or LazyI18nString')

        if not isinstance(address, dict) and type(address).__name__ is not 'LazyI18nString':
            raise TypeError('address is not of instance dict or LazyI18nString')

        if type(name).__name__ is 'LazyI18nString':
            name = utils.LazyI18nToDict(name)

        if type(address).__name__ is 'LazyI18nString':
            address = utils.LazyI18nToDict(address)

        return {
            'kind': 'walletobjects#eventVenue',
            'name': utils.localizedString(name, default),
            'address': utils.localizedString(address, default)
        }

    def message(header: str, localizedHeader: Dict[str, str], body: str, localizedBody: Dict[str, str], default: Optional[str] = None) -> str:
        return {
            'kind': 'walletobjects#walletObjectMessage',
            'header': header,
            'localizedHeader': utils.localizedString(localizedHeader, default),
            'body': body,
            'localizedBody': utils.localizedString(localizedBody, default),
        }

    def pack(string):
        return struct.pack('<Q', len(string))[:4] + bytes(string, 'utf-8')

    def unsealCallback(callbackBody: dict, issuerId: str) -> dict:
        if not isinstance(callbackBody, dict):
            raise TypeError("callbackBody is not a dict or json object")

        if not all(k in callbackBody for k in ('signature', 'intermediateSigningKey', 'protocolVersion', 'signedMessage')):
            raise ValueError("callbackBody does not contain all vital keys: signature, intermediateSigningKey, protocolVersion, signedMessage")

        r = requests.get("https://pay.google.com/gp/m/issuer/keys")

        try:
            pksjson = json.loads(r.content)
        except JSONDecodeError:
            raise ValueError("Could not verify signature: couldn't download public key")

        if 'keys' not in pksjson:
            raise ValueError("Could not verify signature: no public keys in server response")

        webhookValidated = False
        intermediateValidated = False

        for pkjson in pksjson['keys']:
            if int(pkjson['keyExpiration'])/1000 > int(time.time()):
                try:
                    pk = ECC.import_key(base64.b64decode(pkjson['keyValue']))
                except ValueError:
                    break

                # Verify Intermediate Signed Key with Public Key
                verifier = DSS.new(pk, 'fips-186-3', 'der')
                for signature in callbackBody['intermediateSigningKey']['signatures']:
                    try:
                        verifier.verify(
                            SHA256.new(
                                utils.pack('GooglePayPasses') + utils.pack(pkjson['protocolVersion']) +
                                utils.pack(callbackBody['intermediateSigningKey']['signedKey'])
                            ),
                            base64.b64decode(signature)
                        )
                        intermediateValidated = True
                        break
                    except ValueError:
                        pass

                if intermediateValidated:
                    intermediateSigningKey = json.loads(callbackBody['intermediateSigningKey']['signedKey'])

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
                                utils.pack('GooglePayPasses') + utils.pack(str(issuerId)) +
                                utils.pack(callbackBody['protocolVersion']) + utils.pack(callbackBody['signedMessage'])
                            ),
                            base64.b64decode(callbackBody['signature'])
                        )
                        webhookValidated = True
                        break
                    except ValueError:
                        pass

        if intermediateValidated and webhookValidated:
            return json.loads(callbackBody['signedMessage'])
        else:
            raise ValueError("Could not validate signature")
