from walletobjects import eventTicketClass, eventTicketObject, buttonJWT
from walletobjects.constants import (
    reviewStatus, multipleDevicesAndHoldersAllowedStatus, doorsOpen, confirmationCode,
    seat, row, section, gate, objectState, barcode
)


def makeTranslatableStrings(what):
    return {
        'de': "%s DE" % what,
        'en': "%s EN" % what,
        'fr': "%s FR" % what,
    }

#evTclass = eventTicketClass('issuerName', 'classID', multipleDevicesAndHoldersAllowedStatus.multipleHolders, makeTranslatableStrings('Eventname'), reviewStatus.underReview, 'de')

#evTclass.localizedIssuerName(makeTranslatableStrings('IssuerName'))

#evTclass.messages('Header 1', makeTranslatableStrings('Translatable Message Header 1'), 'Body 1', makeTranslatableStrings('Translatable Message Body 1'))
#evTclass.messages('Header 2', makeTranslatableStrings('Translatable Message Header 2'), 'Body 2', makeTranslatableStrings('Translatable Message Body 2'))
#evTclass.messages('Header 3', makeTranslatableStrings('Translatable Message Header 3'), 'Body 3', makeTranslatableStrings('Translatable Message Body 3'))

#evTclass.homepageUri('http://google.com/', 'The Google Search Engine', makeTranslatableStrings('HomepageURI'))
#evTclass.imageModulesData('http://google.com/logo.png', 'The Google Search Engine Logo', makeTranslatableStrings('imageModulesData'))

#evTclass.linksModuleData('http://url1/', 'Description URL 1', makeTranslatableStrings('URL 1'))
#evTclass.linksModuleData('http://url2/', 'Description URL 2', makeTranslatableStrings('URL 2'))
#evTclass.linksModuleData('http://url3/', 'Description URL 3', makeTranslatableStrings('URL 3'))

#evTclass.locations(37.424015499999996, -122.09259560000001)
#evTclass.locations(37.424354, -122.09508869999999)
#evTclass.locations(37.7901435, -122.39026709999997)
#evTclass.locations(40.7406578, -74.00208940000002)

#evTclass.textModulesData('Header 1', 'Body 1', makeTranslatableStrings('textModulesData Header 1'), makeTranslatableStrings('textModulesData Body 1'))
#evTclass.textModulesData('Header 2', 'Body 2', makeTranslatableStrings('textModulesData Header 2'), makeTranslatableStrings('textModulesData Body 2'))

#evTclass.countryCode('de')
#evTclass.hideBarcode(True)
#evTclass.heroImage('http://google.com/logo.png', 'The Hero Image', makeTranslatableStrings('Hero Image'))
#evTclass.hexBackgroundColor('#3B1C4A')
#evTclass.eventId('EventID-Test-123')
#evTclass.logo('http://google.com/logo.png', 'The Logo Image', makeTranslatableStrings('Logo Image'))
#evTclass.venue(makeTranslatableStrings('Venue Name'), makeTranslatableStrings('Venue Address'))

#evTclass.dateTime(doorsOpen.doorsOpen, '1985-04-12T23:20:50.52Z', '1985-04-12T23:20:50.52Z', '1985-04-12T25:20:50.52Z')
#evTclass.dateTime(doorsOpen.gatesOpen, '1985-04-12T23:20:50.52Z', '1985-04-12T23:20:50.52Z', '1985-04-12T25:20:50.52Z')
#evTclass.dateTime(makeTranslatableStrings("Customer Door Open"), '1985-04-12T23:20:50.52Z', '1985-04-12T23:20:50.52Z', '1985-04-12T25:20:50.52Z')

#evTclass.finePrint(makeTranslatableStrings('Fineprint Fineprint Fineprint'))

#evTclass.confirmationCodeLabel(confirmationCode.confirmationCode)
#evTclass.confirmationCodeLabel(confirmationCode.confirmationNumber)
#evTclass.confirmationCodeLabel(confirmationCode.orderNumber)
#evTclass.confirmationCodeLabel(confirmationCode.reservationNumber)
#evTclass.confirmationCodeLabel(makeTranslatableStrings('Custom Conformation Code Label'))

#evTclass.seatLabel(seat.seat)
#evTclass.seatLabel(makeTranslatableStrings('Custom Seat Label'))

#evTclass.rowLabel(row.row)
#evTclass.rowLabel(makeTranslatableStrings('Custom Row Label'))

#evTclass.sectionLabel(section.section)
#evTclass.sectionLabel(makeTranslatableStrings('Custom Section Label'))

#evTclass.gateLabel(gate.gate)
#evTclass.gateLabel(makeTranslatableStrings('Custom Gate Label'))
#print(str(evTclass))
#print(evTclass)
#print(evTclass['eventName']['kind'])

evTobject = eventTicketObject('Object ID here', 'Class ID here', objectState.active, 'DE')
evTobject.barcode(barcode.qrCode, '12345')
print(evTobject)

'''
button = buttonJWT(
    origins=['http://localhost/'],
    issuer='pretix-googlepaypasses@pretix-gpaypasses.iam.gserviceaccount.com'
)

print(button)
'''
print(type(evTobject))
