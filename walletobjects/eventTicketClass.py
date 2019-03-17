import json
from typing import Dict, List, Union

from walletobjects import constants
from walletobjects.utils import utils

class eventTicketClass(dict):
    def __init__(self, issuerName: str, classID: str,
                 multipleDevicesAndHoldersAllowedStatus, eventName: Dict[str, str],
                 reviewStatus: constants.multipleDevicesAndHoldersAllowedStatus, defaultLang: str) -> Dict:
        if not issuerName:
            raise ValueError('issuerName is not provided')

        if not classID:
            raise ValueError('classID is not provided')

        if not hasattr(constants.multipleDevicesAndHoldersAllowedStatus, multipleDevicesAndHoldersAllowedStatus):
            raise TypeError('multipleDevicesAndHoldersAllowedStatus is not of instance walletobjects.constants.multipleDevicesAndHoldersAllowedStatus')

        if not eventName:
            raise ValueError('eventName is not provided')

        if not hasattr(constants.reviewStatus, reviewStatus):
            raise TypeError('reviewStatus is not of instance walletobjects.constants.reviewStatus')

        if not defaultLang:
            raise ValueError('defaultLang is not specified')

        self._defaultLang = defaultLang

        self._eventTicketClass = {
            'kind': 'walletobjects#eventTicketClass',
            'id': classID,
            'issuerName': issuerName,
            'multipleDevicesAndHoldersAllowedStatus': multipleDevicesAndHoldersAllowedStatus,
            'eventName': utils.localizedString(eventName, self._defaultLang),
            'reviewStatus': reviewStatus,
        }

    def localizedIssuerName(self, localizedIssuerName: List[Dict[str, str]]) -> None:
        self._eventTicketClass['localizedIssuerName'] = utils.localizedString(localizedIssuerName, self._defaultLang)

    def messages(self, header: str, localizedHeader: Dict[str, str], body: str, localizedBody: Dict[str, str]) -> None:
        if 'messages' not in self._eventTicketClass:
            self._eventTicketClass['messages'] = []

        self._eventTicketClass['messages'].append(utils.message(header, localizedHeader, body, localizedBody, self._defaultLang))

    def homepageUri(self, uri: str, description: str, localizedDescriptions: List[Dict[str, str]]) -> None:
        self._eventTicketClass['homepageUri'] = utils.localizedUri(uri, description, localizedDescriptions, self._defaultLang)

    def locations(self, latitude: float, longitude: float) -> None:
        if 'locations' not in self._eventTicketClass:
            self._eventTicketClass['locations'] = []

        self._eventTicketClass['locations'].append(utils.latLongPoint(latitude, longitude))

    def infoModuleData(self, infoModuleData) -> None:
        pass

    def imageModulesData(self, uri: str, description: str, localizedDescriptions: List[Dict[str, str]]) -> None:
        self._eventTicketClass['imageModulesData'] = [{
            'mainImage': utils.image(uri, description, localizedDescriptions, self._defaultLang)
        }]

    def textModulesData(self, header: str, body: str, localizedHeader: List[Dict[str, str]], localizedBody: List[Dict[str, str]]) -> None:
        textModule = {
            'header': header,
            'body': body,
            'localizedHeader': utils.localizedString(localizedHeader, self._defaultLang),
            'localizedBody': utils.localizedString(localizedBody, self._defaultLang),
        }

        if not 'textModulesData' in self._eventTicketClass:
            self._eventTicketClass['textModulesData'] = []

        self._eventTicketClass['textModulesData'].append(textModule)


    def linksModuleData(self, uri: str, description: str, localizedDescriptions: Dict[str, str]) -> None:
        if 'linksModuleData' not in self._eventTicketClass:
            self._eventTicketClass['linksModuleData'] = []

        self._eventTicketClass['linksModuleData'].append(utils.localizedUri(uri, description, localizedDescriptions, self._defaultLang))

    def countryCode(self, countryCode: str) -> None:
        self._eventTicketClass['countryCode'] = countryCode

    def hideBarcode(self, hideBarcode: bool) -> None:
        #self._eventTicketClass['hideBarcode'] = bool(hideBarcode)
        # This seems not be working at all.
        pass

    def heroImage(self, uri: str, description: str, localizedDescriptions: List[Dict[str, str]]) -> None:
        self._eventTicketClass['heroImage'] = utils.image(uri, description, localizedDescriptions, self._defaultLang)

    def hexBackgroundColor(self, hexBackgroundColor: str) -> None:
        self._eventTicketClass['hexBackgroundColor'] = hexBackgroundColor

    def eventId(self, eventId: str) -> None:
        self._eventTicketClass['eventId'] = eventId

    def logo(self, uri: str, description: str, localizedDescriptions: List[Dict[str, str]]) -> None:
        self._eventTicketClass['logo'] = utils.image(uri, description, localizedDescriptions, self._defaultLang)

    def venue(self, name: Dict[str, str], address: Dict[str, str]) -> None:
        self._eventTicketClass['venue'] = utils.venue(name, address)

    def dateTime(self, doorsOpenLabel: Union[Dict[str, str], constants.doorsOpen], doorsOpen: str, start: str, end: str) -> None:
        dateTime = {
            'kind': 'walletobjects#eventDateTime',
            'doorsOpen': doorsOpen,
            'start': start,
            'end': end
        }

        try:
            if hasattr(constants.doorsOpen, doorsOpenLabel):
                dateTime['doorsOpenLabel'] = doorsOpenLabel
        except:
            dateTime['customDoorsOpenLabel'] = utils.localizedString(doorsOpenLabel, self._defaultLang)

        self._eventTicketClass['dateTime'] = dateTime

    def finePrint(self, finePrint: Dict[str, str]) -> None:
        self._eventTicketClass['finePrint'] = utils.localizedString(finePrint, self._defaultLang)

    def confirmationCodeLabel(self, confirmationCodeLabel: Union[Dict[str, str], constants.confirmationCode]) -> None:
        try:
            if hasattr(constants.confirmationCode, confirmationCodeLabel):
                self._eventTicketClass['confirmationCodeLabel'] = confirmationCodeLabel
        except:
            self._eventTicketClass['customConfirmationCodeLabel'] = utils.localizedString(confirmationCodeLabel, self._defaultLang)


    def seatLabel(self, seatLabel: Union[Dict[str, str], constants.seat]) -> None:
        try:
            if hasattr(constants.seat, seatLabel):
                self._eventTicketClass['seatLabel'] = seatLabel
        except:
            self._eventTicketClass['customSeatLabel'] = utils.localizedString(seatLabel, self._defaultLang)

    def rowLabel(self, rowLabel: Union[Dict[str, str], constants.row]) -> None:
        try:
            if hasattr(constants.row, rowLabel):
                self._eventTicketClass['rowLabel'] = rowLabel
        except:
            self._eventTicketClass['customRowLabel'] = utils.localizedString(rowLabel, self._defaultLang)


    def sectionLabel(self, sectionLabel: Union[Dict[str, str], constants.section]) -> None:
        try:
            if hasattr(constants.section, sectionLabel):
                self._eventTicketClass['sectionLabel'] = sectionLabel
        except:
            self._eventTicketClass['customSectionLabel'] = utils.localizedString(sectionLabel, self._defaultLang)

    def gateLabel(self, gateLabel: Union[Dict[str, str], constants.gate]) -> None:
        try:
            if hasattr(constants.gate, gateLabel):
                self._eventTicketClass['gateLabel'] = gateLabel
        except:
            self._eventTicketClass['customGateLabel'] = utils.localizedString(gateLabel, self._defaultLang)

    def callbackUrl(self, url):
        self._eventTicketClass['callbackOptions'] = {
            'url': url
        }

    def __getitem__(self, index):
        return self._eventTicketClass[index]

    def __str__(self):
        return json.dumps(self._eventTicketClass, indent=4, sort_keys=True)

    def __len__(self):
        return len(self._eventTicketClass)
