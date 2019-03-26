import json
import time
from typing import Dict, List, Optional

from walletobjects import eventTicketClass, eventTicketObject

class buttonJWT(dict):
    def __init__(
        self, issuer: str, origins: List[str],
        loyaltyClasses: Optional[str] = [], loyaltyObjects: Optional[str] = [],
        offerClasses: Optional[str] = [], offerObjects: Optional[str] = [],
        giftcardClasses: Optional[str] = [], giftcardObjects: Optional[str] = [],
        eventTicketClasses: Optional[eventTicketClass] = [], eventTicketObjects: Optional[eventTicketObject]= [] ,
        flightClasses: Optional[str] = [], flightObjects: Optional[str] = [], skinny: Optional[bool] = False
    ) -> Dict:

        if skinny:
            self._buttonJWT = {
                'iss': issuer,
                'aud': 'google',
                'typ': 'savetoandroidpay',
                'iat': int(time.time()),
                'payload': {
                    'loyaltyClasses': self.skinnify(loyaltyClasses),
                    'loyaltyObjects': self.skinnify(loyaltyObjects),
                    'offerClasses': self.skinnify(offerClasses),
                    'offerObjects': self.skinnify(offerObjects),
                    'giftcardClasses': self.skinnify(giftcardClasses),
                    'giftcardObjects': self.skinnify(giftcardObjects),
                    'eventTicketClasses': self.skinnify(eventTicketClasses),
                    'eventTicketObjects': self.skinnify(eventTicketObjects),
                    'flightClasses': self.skinnify(flightClasses),
                    'flightObjects': self.skinnify(flightObjects),
                },
                'origins': origins
            }
        else:
            self._buttonJWT = {
                'iss': issuer,
                'aud': 'google',
                'typ': 'savetoandroidpay',
                'iat':  int(time.time()),
                'payload': {
                    'loyaltyClasses': loyaltyClasses,
                    'loyaltyObjects': loyaltyObjects,
                    'offerClasses': offerClasses,
                    'offerObjects': offerObjects,
                    'giftcardClasses': giftcardClasses,
                    'giftcardObjects': giftcardObjects,
                    'eventTicketClasses': eventTicketClasses,
                    'eventTicketObjects': eventTicketObjects,
                    'flightClasses': flightClasses,
                    'flightObjects': flightObjects,
                },
                'origins': origins
            }

    def skinnify(self, items):
        skinny = []
        for item in items:
            try:
                skinny.append({
                    "classId": item['classId'],
                    "id": item['id']
                })
            except KeyError:
                skinny.append(item)

        return skinny


    def __getitem__(self, index):
        return self._buttonJWT[index]

    def __str__(self):
        return json.dumps(self._buttonJWT, indent=4, sort_keys=True)