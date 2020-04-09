import json

from walletobjects import constants
from walletobjects import utils


class EventTicketClass(dict):
    def __init__(
            self, issuer_name, class_id, multiple_devices_and_holders_allowed_status, event_name, review_status,
            default_lang
    ):
        if not issuer_name:
            raise ValueError('issuer_name is not provided')

        if not class_id:
            raise ValueError('class_id is not provided')

        if not hasattr(
                constants.MultipleDevicesAndHoldersAllowedStatus,
                str(multiple_devices_and_holders_allowed_status)
        ):
            raise TypeError(
                "multiple_devices_and_holders_allowed_status is not of instance "
                "walletobjects.constants.MultipleDevicesAndHoldersAllowedStatus"
            )

        if not event_name:
            raise ValueError('event_name is not provided')

        if not hasattr(constants.ReviewStatus, str(review_status)):
            raise TypeError('review_status is not of instance walletobjects.constants.reviewStatus')

        if not default_lang:
            raise ValueError('default_lang is not specified')

        self._defaultLang = default_lang

        self._eventTicketClass = {
            'id': class_id,
            'issuerName': issuer_name,
            'multipleDevicesAndHoldersAllowedStatus': multiple_devices_and_holders_allowed_status,
            'eventName': utils.localized_string(event_name, self._defaultLang),
            'reviewStatus': review_status,
        }

    def localized_issuer_name(self, localized_issuer_name):
        self._eventTicketClass['localizedIssuerName'] = utils.localized_string(localized_issuer_name, self._defaultLang)

    def messages(self, header, localized_header, body, localized_body):
        if 'messages' not in self._eventTicketClass:
            self._eventTicketClass['messages'] = []

        self._eventTicketClass['messages'].append(
            utils.message(header, localized_header, body, localized_body, self._defaultLang)
        )

    def homepage_uri(self, uri, description, localized_descriptions):
        self._eventTicketClass['homepageUri'] = utils.localized_uri(
            uri, description, localized_descriptions, self._defaultLang
        )

    def locations(self, latitude, longitude):
        if 'locations' not in self._eventTicketClass:
            self._eventTicketClass['locations'] = []

        self._eventTicketClass['locations'].append(utils.lat_long_point(latitude, longitude))

    def info_module_data(self, info_module_data):
        pass

    def image_modules_data(self, uri, description, localized_descriptions):
        self._eventTicketClass['imageModulesData'] = [{
            'mainImage': utils.image(uri, description, localized_descriptions, self._defaultLang)
        }]

    def text_modules_data(self, header, body, localized_header, localized_body):
        text_module = {
            'header': header,
            'body': body,
            'localizedHeader': utils.localized_string(localized_header, self._defaultLang),
            'localizedBody': utils.localized_string(localized_body, self._defaultLang),
        }

        if 'textModulesData' not in self._eventTicketClass:
            self._eventTicketClass['textModulesData'] = []

        self._eventTicketClass['textModulesData'].append(text_module)

    def links_module_data(self, uri, description, localizedDescriptions):
        if 'linksModuleData' not in self._eventTicketClass:
            self._eventTicketClass['linksModuleData'] = []

        self._eventTicketClass['linksModuleData'].append(
            utils.localized_uri(uri, description, localizedDescriptions, self._defaultLang)
        )

    def country_code(self, country_code):
        self._eventTicketClass['countryCode'] = country_code

    def hide_barcode(self, hide_barcode):
        # self._eventTicketClass['hideBarcode'] = bool(hide_barcode)
        # This seems not be working at all.
        pass

    def hero_image(self, uri, description, localized_descriptions):
        self._eventTicketClass['heroImage'] = utils.image(uri, description, localized_descriptions, self._defaultLang)

    def hex_background_color(self, hex_background_color):
        self._eventTicketClass['hexBackgroundColor'] = hex_background_color

    def event_id(self, event_id):
        self._eventTicketClass['eventId'] = event_id

    def logo(self, uri, description, localized_descriptions):
        self._eventTicketClass['logo'] = utils.image(uri, description, localized_descriptions, self._defaultLang)

    def venue(self, name, address):
        self._eventTicketClass['venue'] = utils.venue(name, address)

    def date_time(self, doors_open_label, doors_open, start, end):
        date_time = {
            'kind': 'walletobjects#eventDateTime',
            'doorsOpen': doors_open,
            'start': start,
            'end': end
        }

        if hasattr(constants.DoorsOpen, str(doors_open_label)):
            date_time['doorsOpenLabel'] = doors_open_label
        else:
            date_time['customDoorsOpenLabel'] = utils.localized_string(doors_open_label, self._defaultLang)

        self._eventTicketClass['dateTime'] = date_time

    def fine_print(self, fine_print):
        self._eventTicketClass['finePrint'] = utils.localized_string(fine_print, self._defaultLang)

    def confirmation_code_label(self, confirmation_code_label):
        if hasattr(constants.ConfirmationCode, str(confirmation_code_label)):
            self._eventTicketClass['confirmationCodeLabel'] = confirmation_code_label
        else:
            self._eventTicketClass['customConfirmationCodeLabel'] = utils.localized_string(
                confirmation_code_label, self._defaultLang
            )

    def seat_label(self, seat_label):
        if hasattr(constants.Seat, str(seat_label)):
            self._eventTicketClass['seatLabel'] = seat_label
        else:
            self._eventTicketClass['customSeatLabel'] = utils.localized_string(seat_label, self._defaultLang)

    def row_label(self, row_label):
        if hasattr(constants.Row, str(row_label)):
            self._eventTicketClass['rowLabel'] = row_label
        else:
            self._eventTicketClass['customRowLabel'] = utils.localized_string(row_label, self._defaultLang)

    def section_label(self, section_label):
        if hasattr(constants.Section, str(section_label)):
            self._eventTicketClass['sectionLabel'] = section_label
        else:
            self._eventTicketClass['customSectionLabel'] = utils.localized_string(section_label, self._defaultLang)

    def gate_label(self, gate_label):
        if hasattr(constants.Gate, str(gate_label)):
            self._eventTicketClass['gateLabel'] = gate_label
        else:
            self._eventTicketClass['customGateLabel'] = utils.localized_string(gate_label, self._defaultLang)

    def callback_url(self, callback_url):
        self._eventTicketClass['callbackOptions'] = {
            'url': callback_url
        }

    def __getitem__(self, index):
        return self._eventTicketClass[index]

    def __str__(self):
        return json.dumps(self._eventTicketClass, indent=4, sort_keys=True)

    def __len__(self):
        return len(self._eventTicketClass)
