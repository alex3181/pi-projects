# enable i2c interface in raspi-config
# pip install rpi_lcd, requests

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from rpi_lcd import LCD
from time import sleep

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
parameters = {"start": "1", "limit": "150", "convert": "USD"}
headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "02e9907d-56c4-46c6-a9c7-d14c7af53f6f",
}

session = Session()
session.headers.update(headers)
lcd = LCD()

try:
    while True:
        # pull data
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        price_BTC = data["data"][0]["quote"]["USD"]["price"]
        price_ETH = data["data"][1]["quote"]["USD"]["price"]
        # print(f"${price:,.2f}")
        prices = {}
        for crypto in data["data"]:
            if crypto["name"] == "Bitcoin":
                prices["Bitcoin"] = crypto["quote"]["USD"]["price"]
            elif crypto["name"] == "Ethereum":
                prices["Ethereum"] = crypto["quote"]["USD"]["price"]
            elif crypto["name"] == "Litecoin":
                prices["Litecoin"] = crypto["quote"]["USD"]["price"]
            elif crypto["name"] == "Bitcoin Cash":
                prices["Bitcoin Cash"] = crypto["quote"]["USD"]["price"]

        for key, value in prices.items():
            lcd.text(key, 1, "center")
            lcd.text(f"${value:,.2f}", 2, "center")
            sleep(5)
        # display on screen


except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)
finally:
    lcd.clear()
