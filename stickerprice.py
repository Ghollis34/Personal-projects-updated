import json
from datetime import datetime

from nacl.bindings import crypto_sign
import requests

# replace with your api keys
public_key = "749f9b22a4112477895d654660951770444e9b238cd4e72572634406f4f725e0"
secret_key = "08870e6af61502e02c74a75d0f017dd15619f5929ed2b9921057510c7668aeef749f9b22a4112477895d654660951770444e9b238cd4e72572634406f4f725e0"

# change url to prod
rootApiUrl = "https://api.dmarket.com"


def stockholm_contenders():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Stockholm+Contender")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]
def stockholm_challengers():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Stockholm+Challengers")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]


exchange_rate = 0.82

stockholm_contenders_price = float(stockholm_contenders()["price"]["USD"]) / 100
stock_cont_price_in_gbp = stockholm_contenders_price * exchange_rate
stock_cont_formatted_price = "{:.2f}".format(stock_cont_price_in_gbp)
print("Price of stockholm contenders: £" + stock_cont_formatted_price)

stockholm_challengers_price = float(stockholm_challengers()["price"]["USD"]) / 100
stock_chall_price_in_gbp = stockholm_challengers_price * exchange_rate
stock_chall_formatted_price = "{:.2f}".format(stock_chall_price_in_gbp)
print("Price of stockholm challengers: £" + stock_chall_formatted_price)


