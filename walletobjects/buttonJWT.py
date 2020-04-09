import json
import time


class ButtonJWT(dict):
    def __init__(
            self, issuer, origins, loyalty_classes=None, loyalty_objects=None, offer_classes=None, offer_objects=None,
            giftcard_classes=None, giftcard_objects=None, event_ticket_classes=None, event_ticket_objects=None,
            flight_classes=None, flight_objects=None, skinny=False
    ):

        if skinny:
            self._button_jwt = {
                'iss': issuer,
                'aud': 'google',
                'typ': 'savetoandroidpay',
                'iat': int(time.time()),
                'payload': {
                    'loyaltyClasses': self.skinnify(loyalty_classes),
                    'loyaltyObjects': self.skinnify(loyalty_objects),
                    'offerClasses': self.skinnify(offer_classes),
                    'offerObjects': self.skinnify(offer_objects),
                    'giftcardClasses': self.skinnify(giftcard_classes),
                    'giftcardObjects': self.skinnify(giftcard_objects),
                    'eventTicketClasses': self.skinnify(event_ticket_classes),
                    'eventTicketObjects': self.skinnify(event_ticket_objects),
                    'flightClasses': self.skinnify(flight_classes),
                    'flightObjects': self.skinnify(flight_objects),
                },
                'origins': origins
            }
        else:
            self._button_jwt = {
                'iss': issuer,
                'aud': 'google',
                'typ': 'savetoandroidpay',
                'iat':  int(time.time()),
                'payload': {
                    'loyaltyClasses': loyalty_classes,
                    'loyaltyObjects': loyalty_objects,
                    'offerClasses': offer_classes,
                    'offerObjects': offer_objects,
                    'giftcardClasses': giftcard_classes,
                    'giftcardObjects': giftcard_objects,
                    'eventTicketClasses': event_ticket_classes,
                    'eventTicketObjects': event_ticket_objects,
                    'flightClasses': flight_classes,
                    'flightObjects': flight_objects,
                },
                'origins': origins
            }

    def skinnify(self, items):
        skinny = []

        if isinstance(items, list):
            for item in items:
                try:
                    skinny.append({
                        "classId": item['classId'],
                        "id": item['id']
                    })
                except KeyError:
                    skinny.append(item)
        else:
            skinny.append(items)

        return skinny

    def __getitem__(self, index):
        return self._button_jwt[index]

    def __str__(self):
        return json.dumps(self._button_jwt, indent=4, sort_keys=True)
