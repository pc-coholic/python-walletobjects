from typing import Dict, Optional

class utils(object):
    def LazyI18nToDict(LazyI18nString) -> Dict[str, str]:
        return LazyI18nString.data

    def localizedString(stringsDict: Dict[str, str], default: Optional[str]=None) -> str:
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

    def localizedUri(uri: str, description: str, stringsDict: Dict[str, str], default: Optional[str]=None) -> str:
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

    def image(uri: str, description: str, stringsDict: Dict[str, str], default: Optional[str]=None) -> str:
        if not isinstance(stringsDict, dict) and type(stringsDict).__name__ is not 'LazyI18nString':
            raise TypeError('localizedString is not of instance dict or LazyI18nString')

        if type(stringsDict).__name__ is 'LazyI18nString':
            stringsDict = utils.LazyI18nToDict(stringsDict)

        return {
            'kind': 'walletobjects#image',
            'sourceUri': utils.localizedUri(uri, description, stringsDict)
        }

    def venue(name: Dict[str, str], address: Dict[str, str], default: Optional[str]=None) -> str:
        if not isinstance(name, dict) and type(stringsDict).__name__ is not 'LazyI18nString':
            raise TypeError('name is not of instance dict or LazyI18nString')

        if not isinstance(address, dict) and type(stringsDict).__name__ is not 'LazyI18nString':
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

    def message(header: str, localizedHeader: Dict[str, str], body: str, localizedBody: Dict[str, str], default: Optional[str]=None) -> str:
        return {
            'kind': 'walletobjects#walletObjectMessage',
            'header': header,
            'localizedHeader': utils.localizedString(localizedHeader, default),
            'body': body,
            'localizedBody': utils.localizedString(localizedHeader, default),
        }
