import json

from walletobjects import constants, utils


class EventTicketObject(dict):
    def __init__(self, object_id, class_id, object_state, default_lang):
        if not object_id:
            raise ValueError('object_id is not provided')

        if not class_id:
            raise ValueError('class_id is not provided')

        if not hasattr(constants.ObjectState, str(object_state)):
            raise TypeError('object_state is not of instance walletobjects.constants.objectState')

        if not default_lang:
            raise ValueError('default_lang is not specified')

        self._defaultLang = default_lang

        self._eventTicketObject = {
            'kind': 'walletobjects#eventTicketObject',
            'id': object_id,
            'classId': class_id,
            'state': object_state,
        }

    def barcode(self, barcode_type, value, alternate_text=None):
        if not hasattr(constants.Barcode, str(barcode_type)):
            raise TypeError('barcode is not of instance walletobjects.constants.barcode')

        self._eventTicketObject['barcode'] = {
            'kind': 'walletobjects#barcode',
            'type': barcode_type,
            'value': value,
            'alternateText': alternate_text if alternate_text else "",
        }

    '''
    def messages(self, header, localized_header, body:, localized_body):
        if 'messages' not in self._eventTicketObject:
            self._eventTicketObject['messages'] = []

        self._eventTicketObject['messages'].append(
            utils.message(header, localized_header, body, localized_body, self._defaultLang)
        )
    '''
    def valid_time_interval(self, valid_time_interval):
        pass

    def locations(self, latitude, longitude):
        if 'locations' not in self._eventTicketObject:
            self._eventTicketObject['locations'] = []

        self._eventTicketObject['locations'].append(utils.lat_long_point(latitude, longitude))

    def disable_expiration_notification(self, disable_expiration_notification):
        self._eventTicketObject['disableExpirationNotification'] = bool(disable_expiration_notification)
        pass

    def info_module_data(self, info_module_data):
        pass

    def image_modules_data(self, uri, description, localized_descriptions):
        self._eventTicketObject['imageModulesData'] = [{
            'mainImage': utils.image(uri, description, localized_descriptions, self._defaultLang)
        }]

    def text_modules_data(self, header, body, localized_header, localized_body):
        text_module = {
            'header': header,
            'body': body,
            'localizedHeader': utils.localized_string(localized_header, self._defaultLang),
            'localizedBody': utils.localized_string(localized_body, self._defaultLang),
        }

        if not 'textModulesData' in self._eventTicketObject:
            self._eventTicketObject['textModulesData'] = []

        self._eventTicketObject['textModulesData'].append(text_module)

    def links_module_data(self, uri, description, localized_descriptions):
        if 'linksModuleData' not in self._eventTicketObject:
            self._eventTicketObject['linksModuleData'] = []

        self._eventTicketObject['linksModuleData'].append(
            utils.localized_uri(uri, description, localized_descriptions, self._defaultLang)
        )

    def seat(self, seat):
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['seat'] = utils.localized_string(seat, self._defaultLang)

    def row(self, row):
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['row'] = utils.localized_string(row, self._defaultLang)

    def section(self, section):
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['section'] = utils.localized_string(section, self._defaultLang)

    def gate(self, gate):
        if 'seatInfo' not in self._eventTicketObject:
            self._eventTicketObject['seatInfo'] = {
                'kind': 'walletobjects#eventSeat'
            }

        self._eventTicketObject['seatInfo']['gate'] = utils.localized_string(gate, self._defaultLang)

    def reservation_info(self, reservation_info):
        self._eventTicketObject['reservationInfo'] = {
            'kind': 'walletobjects#eventReservationInfo',
            'confirmationCode': reservation_info,
        }

    def ticket_holder_name(self, ticket_holder_name):
        self._eventTicketObject['ticketHolderName'] = ticket_holder_name

    def ticket_number(self, ticket_number):
        self._eventTicketObject['ticketNumber'] = ticket_number

    def ticket_type(self, ticket_type):
        self._eventTicketObject['ticketType'] = utils.localized_string(ticket_type, self._defaultLang)

    def face_value(self, face_value, currency_code):
        self._eventTicketObject['faceValue'] = {
            'kind': 'walletobjects#money',
            'micros': int(face_value),
            'currencyCode': currency_code,
        }

    def __getitem__(self, index):
        return self._eventTicketObject[index]

    def __str__(self):
        return json.dumps(self._eventTicketObject, indent=4, sort_keys=True)

    def __len__(self):
        return len(self._eventTicketObject)
