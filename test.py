from walletobjects import EventTicketClass, EventTicketObject
from walletobjects.constants import (Barcode, ConfirmationCode, DoorsOpen,
                                     Gate,
                                     MultipleDevicesAndHoldersAllowedStatus,
                                     ObjectState, ReviewStatus, Row, Seat,
                                     Section)


def make_translatable_strings(what):
    return {
        'de': "%s DE" % what,
        'en': "%s EN" % what,
        'fr': "%s FR" % what,
    }


evt_class = EventTicketClass(
    'issuerName',
    'classID',
    MultipleDevicesAndHoldersAllowedStatus.multipleHolders,
    make_translatable_strings('Eventname'),
    ReviewStatus.underReview,
    'de'
)

evt_class.localized_issuer_name(make_translatable_strings('IssuerName'))

evt_class.messages(
    'Header 1',
    make_translatable_strings('Translatable Message Header 1'),
    'Body 1',
    make_translatable_strings('Translatable Message Body 1')
)

evt_class.messages(
    'Header 2',
    make_translatable_strings('Translatable Message Header 2'),
    'Body 2',
    make_translatable_strings('Translatable Message Body 2')
)

evt_class.messages(
    'Header 3',
    make_translatable_strings('Translatable Message Header 3'),
    'Body 3',
    make_translatable_strings('Translatable Message Body 3')
)

evt_class.homepage_uri(
    'http://google.com/',
    'The Google Search Engine',
    make_translatable_strings('HomepageURI')
)
evt_class.image_modules_data(
    'http://google.com/logo.png',
    'The Google Search Engine Logo',
    make_translatable_strings('imageModulesData')
)

evt_class.links_module_data(
    'http://url1/',
    'Description URL 1',
    make_translatable_strings('URL 1')
)

evt_class.links_module_data(
    'http://url2/',
    'Description URL 2',
    make_translatable_strings('URL 2')
)

evt_class.links_module_data(
    'http://url3/',
    'Description URL 3',
    make_translatable_strings('URL 3')
)

evt_class.locations(37.424015499999996, -122.09259560000001)
evt_class.locations(37.424354, -122.09508869999999)
evt_class.locations(37.7901435, -122.39026709999997)
evt_class.locations(40.7406578, -74.00208940000002)

evt_class.text_modules_data(
    'Header 1',
    'Body 1',
    make_translatable_strings('textModulesData Header 1'),
    make_translatable_strings('textModulesData Body 1')
)

evt_class.text_modules_data(
    'Header 2',
    'Body 2',
    make_translatable_strings('textModulesData Header 2'),
    make_translatable_strings('textModulesData Body 2')
)

evt_class.country_code('de')

evt_class.hide_barcode(True)

evt_class.hero_image(
    'http://google.com/logo.png',
    'The Hero Image',
    make_translatable_strings('Hero Image')
)

evt_class.hex_background_color('#3B1C4A')

evt_class.event_id('EventID-Test-123')

evt_class.logo(
    'http://google.com/logo.png',
    'The Logo Image',
    make_translatable_strings('Logo Image')
)

evt_class.venue(
    make_translatable_strings('Venue Name'),
    make_translatable_strings('Venue Address')
)

evt_class.date_time(
    DoorsOpen.doorsOpen,
    '1985-04-12T23:20:50.52Z',
    '1985-04-12T23:20:50.52Z',
    '1985-04-12T25:20:50.52Z'
)

evt_class.date_time(
    DoorsOpen.gatesOpen,
    '1985-04-12T23:20:50.52Z',
    '1985-04-12T23:20:50.52Z',
    '1985-04-12T25:20:50.52Z'
)

evt_class.date_time(
    make_translatable_strings("Customer Door Open"),
    '1985-04-12T23:20:50.52Z',
    '1985-04-12T23:20:50.52Z',
    '1985-04-12T25:20:50.52Z'
)

evt_class.fine_print(make_translatable_strings('Fineprint Fineprint Fineprint'))

evt_class.confirmation_code_label(ConfirmationCode.confirmationCode)

evt_class.confirmation_code_label(ConfirmationCode.confirmationNumber)

evt_class.confirmation_code_label(ConfirmationCode.orderNumber)

evt_class.confirmation_code_label(ConfirmationCode.reservationNumber)

evt_class.confirmation_code_label(make_translatable_strings('Custom Conformation Code Label'))

evt_class.seat_label(Seat.seat)

evt_class.seat_label(make_translatable_strings('Custom Seat Label'))

evt_class.row_label(Row.row)

evt_class.row_label(make_translatable_strings('Custom Row Label'))

evt_class.section_label(Section.section)

evt_class.section_label(make_translatable_strings('Custom Section Label'))

evt_class.gate_label(Gate.gate)

evt_class.gate_label(make_translatable_strings('Custom Gate Label'))

print(str(evt_class))
print(evt_class)
print(evt_class['eventName']['kind'])

evt_object = EventTicketObject(
    'Object ID here',
    'Class ID here',
    ObjectState.active,
    'DE'
)

evt_object.barcode(Barcode.qrCode, '12345')

print(evt_object)

'''
button = buttonJWT(
    origins=['http://localhost/'],
    issuer='pretix-googlepaypasses@pretix-gpaypasses.iam.gserviceaccount.com'
)

print(button)
'''
print(type(evt_object))
