class MultipleDevicesAndHoldersAllowedStatus(object):
    multipleHolders = 'multipleHolders'
    oneUserAllDevices = 'oneUserAllDevices'
    oneUserOneDevice = 'oneUserOneDevice'


class ReviewStatus(object):
    approved = 'approved'
    draft = 'draft'
    rejected = 'rejected'
    underReview = 'underReview'


class DoorsOpen(object):
    doorsOpen = 'doorsOpen'
    gatesOpen = 'gatesOpen'


class ConfirmationCode(object):
    confirmationCode = 'confirmationCode'
    confirmationNumber = 'confirmationNumber'
    orderNumber = 'orderNumber'
    reservationNumber = 'reservationNumber'


class Seat(object):
    seat = 'seat'


class Row(object):
    row = 'row'


class Section(object):
    section = 'section'
    theater = 'theater'


class Gate(object):
    gate = 'gate'
    entrance = 'entrance'
    door = 'door'


class ObjectState(object):
    active = 'active'
    completed = 'completed'
    expired = 'expired'
    inactive = 'inactive'


class Barcode(object):
    aztec = 'aztec'
    codabar = 'codabar'
    code128 = 'code128'
    code39 = 'code39'
    dataMatrix = 'dataMatrix'
    ean13 = 'ean13'
    ean8 = 'ean8'
    itf14 = 'itf14'
    pdf417 = 'pdf417'
    qrCode = 'qrCode'
    textOnly = 'textOnly'
    upcA = 'upcA'
    upcE = 'upcE'
