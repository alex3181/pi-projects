import yfinance as yf

# Define the stock indices we are interested in
indices = {"S&P 500": "^GSPC", "Dow Jones": "^DJI", "NASDAQ": "^IXIC"}


def get_real_time_data():
    data = {}
    for name, ticker in indices.items():
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1d")
        if not hist.empty:
            data[name] = {
                "Current Price": hist["Close"].iloc[-1],
                "Open": hist["Open"].iloc[-1],
                "High": hist["High"].iloc[-1],
                "Low": hist["Low"].iloc[-1],
                "Volume": hist["Volume"].iloc[-1],
            }
        else:
            data[name] = "No data available"
    return data


if __name__ == "__main__":
    real_time_data = get_real_time_data()
    for index, info in real_time_data.items():
        print(f"{index}:")
        if isinstance(info, dict):
            for key, value in info.items():
                print(f"  {key}: {value}")
        else:
            print(f"  {info}")
        print()
