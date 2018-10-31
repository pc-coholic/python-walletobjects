import json
import time
from typing import Dict, List, Union, Optional

from walletobjects import constants
from walletobjects import eventTicketClass, eventTicketObject

class buttonJWT(dict):
    def __init__(
        self, issuer: str, origins: List[str],
        loyaltyClasses: Optional[str]=[], loyaltyObjects: Optional[str]=[],
        offerClasses: Optional[str]=[], offerObjects: Optional[str]=[],
        giftcardClasses: Optional[str]=[], giftcardObjects: Optional[str]=[],
        eventTicketClasses: Optional[eventTicketClass]=[], eventTicketObjects: Optional[eventTicketObject]=[],
        flightClasses: Optional[str]=[], flightObjects: Optional[str]=[],
    ) -> Dict:

        self._buttonJWT = {
            'iss': issuer,
            'aud': 'google',
            'typ': 'savetoandroidpay',
            'iat':  int(time.time()),
            'payload': {
#                'webserviceResponse': {
#                    'result': 'approved',
#                    'message': 'Success.'
#                },
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
            'origins' : origins
        }

    def __getitem__(self, index):
        return self._buttonJWT[index]

    def __str__(self):
        return json.dumps(self._buttonJWT, indent=4, sort_keys=True)
