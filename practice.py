import requests
import secret


def run():
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=GSPC&interval=5min&apikey={secret.ALPHA_VINTAGE_API}"
    r = requests.get(url)
    data = r.json()
    print(data)


if __name__ == "__main__":
    run()
