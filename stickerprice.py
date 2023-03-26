import json
import configparser
import requests

# replace with your api keys
public_key = "749f9b22a4112477895d654660951770444e9b238cd4e72572634406f4f725e0"
secret_key = "08870e6af61502e02c74a75d0f017dd15619f5929ed2b9921057510c7668aeef749f9b22a4112477895d654660951770444e9b238cd4e72572634406f4f725e0"

# change url to prod
rootApiUrl = "https://api.dmarket.com"

config = configparser.ConfigParser()
config.read("C:\Config\config.ini")

bought_stock_chall = config.getfloat('prices', 'stock_chall')
bought_stock_con = config.getfloat('prices', 'stock_con')
bought_ant_chall = config.getfloat('prices', 'ant_chall')
bought_rio_leg = config.getfloat('prices', 'rio_leg')
bought_rio_chall = config.getfloat('prices', 'rio_chall')

number_of_rio_leg = config.getint('number_bought', 'rio_leg')
number_of_rio_chall = config.getint('number_bought', 'rio_chall')
number_of_stock_chall = config.getint('number_bought', 'stock_chall')
number_of_stock_con = config.getint('number_bought', 'stock_con')
number_of_ant_chall = config.getint('number_bought', 'ant_chall')

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    exchange_rate = data["rates"]["GBP"]
    return(exchange_rate)

def stockholm_contenders():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Stockholm+Contender&sort=price&order=asc")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]
def stockholm_challengers():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Stockholm+Challengers&sort=price&order=asc")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]

def antwerp_challengers():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Antwerp+Challengers&sort=price&order=asc")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]

def rio_legends():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Rio+Legends&sort=price&order=asc")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]

def rio_challengers():
    market_response = requests.get(rootApiUrl + "/exchange/v1/market/items?gameId=a8db&limit=1&currency=USD&title=Rio+Challenger&sort=price&order=asc")
    offers = json.loads(market_response.text)["objects"]
    return offers[0]


stock_con = float(stockholm_contenders()["price"]["USD"]) / 100 * get_exchange_rate()
print("Current price of Stockholm Contenders: " + "£{:.2f}".format(stock_con))
stonks_stock_con = ((float(stock_con) - bought_stock_con)/bought_stock_con)*100
print("Stockholm Contenders percentage gain = " + "{:.2f}".format(stonks_stock_con) + "%")

stock_chall = float(stockholm_challengers()["price"]["USD"]) / 100 * get_exchange_rate()
print("Current price of Stockholm Challengers: " + "£{:.2f}".format(stock_chall))
stonks_stock_chall = ((float(stock_chall) - bought_stock_chall)/bought_stock_chall)*100
print("Stockholm Contenders percentage gain = " + "{:.2f}".format(stonks_stock_chall) + "%")

ant_chall = float(antwerp_challengers()["price"]["USD"]) / 100 * get_exchange_rate()
print("Current price of Antwerp Challengers: " + "£{:.2f}".format(ant_chall))
stonks_ant_chall = ((float(ant_chall) - bought_ant_chall)/bought_ant_chall)*100
print("Antwerp Challengers percentage gain = " + "{:.2f}".format(stonks_ant_chall) + "%")

rio_leg = float(rio_legends()["price"]["USD"]) / 100 * get_exchange_rate()
print("Current price of Rio Legends: " + "£{:.2f}".format(rio_leg))
stonks_rio_leg = ((float(rio_leg) - bought_rio_leg)/bought_rio_leg)*100
print("Rio Legends percentage gain = " + "{:.2f}".format(stonks_rio_leg) + "%")

rio_chall = float(rio_challengers()["suggestedPrice"]["USD"]) / 100 * get_exchange_rate()
print("Current price of Rio Challengers: " + "£{:.2f}".format(rio_chall))
stonks_rio_chall = ((float(rio_chall) - bought_rio_chall)/bought_rio_chall)*100
print("Rio Challengers percentage gain = " + "{:.2f}".format(stonks_rio_chall) + "%")

total_money_gain = ((stock_con*number_of_stock_con) + (stock_chall*number_of_stock_chall) + (ant_chall*number_of_ant_chall) + (rio_leg*number_of_rio_leg) + (rio_chall*number_of_rio_chall))
print("Total money gain:" + " £{:.2f}".format(total_money_gain-1000))
total_percentage_gain = ((total_money_gain - 1000)/1000)*100
print("Total percentage gain:" + " {:.2f}".format(total_percentage_gain) + "%")
