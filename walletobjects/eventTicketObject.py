import json
from typing import Dict, List, Union

from walletobjects import constants
from walletobjects.utils import utils

class eventTicketObject(dict):
    def __init__(self, objectID: str, classID: str, objectState: constants.objectState, defaultLang: str) -> Dict:
        if not objectID:
            raise ValueError('objectID is not provided')

        if not classID:
            raise ValueError('classID is not provided')

        if not hasattr(constants.objectState, objectState):
            raise TypeError('objectState is not of instance walletobjects.constants.objectState')

        if not defaultLang:
            raise ValueError('defaultLang is not specified')

        self._defaultLang = defaultLang

        self._eventTicketObject = {
            'kind': 'walletobjects#eventTicketObject',
            'id': objectID,
            'classId': classID,
            'state': objectState,
        }

    def barcode(self, type: constants.barcode, value: str, alternateText: str = None) -> None:
        if not hasattr(constants.barcode, type):
            raise TypeError('barcode is not of instance walletobjects.constants.barcode')

        self._eventTicketObject['barcode'] = {
            'kind': 'walletobjects#barcode',
            'type': type,
            'value': value,
            'alternateText': alternateText if alternateText else "",
        }

    '''
    def messages(self, header: str, localizedHeader: Dict[str, str], body: str, localizedBody: Dict[str, str]) -> None:
        if 'messages' not in self._eventTicketObject:
            self._eventTicketObject['messages'] = []

        self._eventTicketObject['messages'].append(utils.message(header, localizedHeader, body, localizedBody, self._defaultLang))
    '''
    def validTimeInterval(self, validTimeInterval) -> None:
        pass

    def locations(self, latitude: float, longitude: float) -> None:
        if 'locations' not in self._eventTicketObject:
            self._eventTicketObject['locations'] = []

        self._eventTicketObject['locations'].append(utils.latLongPoint(latitude, longitude))

    def disableExpirationNotification(self, disableExpirationNotification: bool) -> None:
        self._eventTicketObject['disableExpirationNotification'] = bool(disableExpirationNotification)
        pass

    def infoModuleData(self, infoModuleData) -> None:
        pass

    def imageModulesData(self, uri: str, description: str, localizedDescriptions: List[Dict[str, str]]) -> None:
        self._eventTicketObject['imageModulesData'] = [{
            'mainImage': utils.image(uri, description, localizedDescriptions, self._defaultLang)
        }]

    def textModulesData(self, header: str, body: str, localizedHeader: List[Dict[str, str]], localizedBody: List[Dict[str, str]]) -> None:
        textModule = {
            'header': header,
            'body': body,
            'localizedHeader': utils.localizedString(localizedHeader, self._defaultLang),
            'localizedBody': utils.localizedString(localizedBody, self._defaultLang),
        }

        if not 'textModulesData' in self._eventTicketObject:
            self._eventTicketObject['textModulesData'] = []

        self._eventTicketObject['textModulesData'].append(textModule)

    def linksModuleData(self, uri: str, description: str, localizedDescriptions: Dict[str, str]) -> None:
        if 'linksModuleData' not in self._eventTicketObject:
            self._eventTicketObject['linksModuleData'] = []

        self._eventTicketObject['linksModuleData'].append(utils.localizedUri(uri, description, localizedDescriptions, self._defaultLang))

    def seat(self, seat: str) -> None:
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['seat'] = utils.localizedString(seat, self._defaultLang)

    def row(self, row: str) -> None:
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['row'] = utils.localizedString(row, self._defaultLang)

    def row(self, section: str) -> None:
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['section'] = utils.localizedString(section, self._defaultLang)

    def gate(self, gate: str) -> None:
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['gate'] = utils.localizedString(gate, self._defaultLang)

    def reservationInfo(self, reservationInfo: str) -> None:
        self._eventTicketObject['reservationInfo'] = {
            'kind': 'walletobjects#eventReservationInfo',
            'confirmationCode': reservationInfo,
        }

    def ticketHolderName(self, ticketHolderName: str) -> None:
        self._eventTicketObject['ticketHolderName'] = ticketHolderName

    def ticketNumber(self, ticketNumber: str) -> None:
        self._eventTicketObject['ticketNumber'] = ticketNumber

    def ticketType(self, ticketType: List[Dict[str, str]]) -> None:
        self._eventTicketObject['ticketType'] = utils.localizedString(ticketType, self._defaultLang)

    def faceValue(self, faceValue: int, currencyCode: str) -> None:
        self._eventTicketObject['faceValue'] = {
            'kind': 'walletobjects#money',
            'micros': int(faceValue),
            'currencyCode': currencyCode,
        }

    def __getitem__(self, index):
        return self._eventTicketObject[index]

    def __str__(self):
        return json.dumps(self._eventTicketObject, indent=4, sort_keys=True)

    def __len__(self):
        return len(self._eventTicketObject)
