import json
from json import JSONDecodeError

import constants
from google.auth import crypt, jwt

from google.auth.transport.requests import AuthorizedSession
from google.oauth2 import service_account


class Comms(object):
    def __init__(self, settings):
        if isinstance(settings, str):
            try:
                settings = json.loads(settings)
            except JSONDecodeError:
                pass

        if not isinstance(settings, dict):
            raise Exception('Could not parse settings into JSON-dict')

        try:
            credentials = service_account.Credentials.from_service_account_info(
                settings,
                scopes=['https://www.googleapis.com/auth/wallet_object.issuer'],
            )

            self.__session = AuthorizedSession(credentials)
            self.__signer = crypt.RSASigner.from_service_account_info(settings)
            self.client_email = settings.get('client_email')
        except ValueError:
            raise Exception('Could not setup Comms. Did you properly setup the necessary credentials?')

    def get_item(self, item_type, item_name):
        if not (hasattr(constants.ClassType, str(item_type)) or hasattr(constants.ObjectType, str(item_type))):
            raise Exception('Invalid Class or Object Type')

        result = self.__session.get(
            'https://walletobjects.googleapis.com/walletobjects/v1/%s/%s' % (item_type, item_name)
        )

        if result.status_code == 200:
            return result.json()
        elif result.status_code == 404:
            return False
        else:
            return None

    def put_item(self, item_type, item_name, payload):
        if not (hasattr(constants.ClassType, str(item_type)) or hasattr(constants.ObjectType, str(item_type))):
            raise Exception('Invalid Class or Object Type')

        item = self.get_item(item_type, item_name)

        if item is None:
            raise Exception('API Error')
        elif not item:
            result = self.__session.post(
                'https://walletobjects.googleapis.com/walletobjects/v1/%s?strict=true' % item_type,
                json=json.loads(str(payload))
            )
        else:
            result = self.__session.put(
                'https://walletobjects.googleapis.com/walletobjects/v1/%s/%s?strict=true' % (item_type, item_name),
                json=json.loads(str(payload))
            )

        result.raise_for_status()

        return result.json()

    def sign_jwt(self, payload):
        payload = json.loads(str(payload))
        encoded = jwt.encode(self.__signer, payload)

        if not encoded:
            return False

        return encoded.decode("utf-8")
