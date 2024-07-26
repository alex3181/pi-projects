import requests


def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}

    response = requests.get(url, params=params)
    data = response.json()

    if "bitcoin" in data:
        return data["bitcoin"]["usd"]
    else:
        return None


if __name__ == "__main__":
    price = get_bitcoin_price()
    if price:
        print(f"The current price of Bitcoin is ${price:.2f} USD")
    else:
        print("Failed to retrieve Bitcoin price")
