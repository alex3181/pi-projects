import sys
import datetime
import pyautogui
import yfinance as yf


from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class window(QWidget):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)

        font_family = "Helvetica"  # "Arial"

        date_font = QFont()
        date_font.setFamily(font_family)
        date_font.setPointSize(35)
        date_font.bold()

        day_of_week_font = QFont()
        day_of_week_font.setFamily(font_family)
        day_of_week_font.setPointSize(35)
        day_of_week_font.bold()

        time_font = QFont()
        time_font.setFamily(font_family)
        time_font.setPointSize(70)
        time_font.bold()

        price_font = QFont()
        price_font.setFamily(font_family)
        price_font.setPointSize(25)
        price_font.bold()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgb(220, 220, 220);")

        # Set up a main Layout. It will be vertical
        self.main_layout = QVBoxLayout()

        # Set up a date and time Layout. It will be horizontal
        self.date_time_layout = QHBoxLayout()

        # Set up a date Layout. It will be vertical
        self.date_layout = QVBoxLayout()

        # Set up 3 information layouts. They will be horizontal
        self.info_layout_1 = QHBoxLayout()
        self.info_layout_1.setContentsMargins(50, 0, 0, 0)
        self.info_layout_2 = QHBoxLayout()
        self.info_layout_2.setContentsMargins(50, 0, 0, 0)
        self.info_layout_3 = QHBoxLayout()
        self.info_layout_3.setContentsMargins(50, 0, 0, 0)

        # create time label
        self.time_label = QLabel(self)
        self.time_label.setFont(time_font)
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # create date label
        self.date_label = QLabel(self)
        self.date_label.setFont(date_font)
        self.date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # create day of week label
        self.week_day_label = QLabel(self)
        self.week_day_label.setFont(day_of_week_font)
        self.week_day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        logo_height = 50
        logo_label_width = 50
        info_widget_height = 50
        clock_label_height = 160

        # create label with bitcoin logo
        self.bitcoin_logo_label = QLabel(self)
        pixmap = QPixmap("images/bitcoin.png")
        pixmap_resized = pixmap.scaledToHeight(logo_height)
        self.bitcoin_logo_label.setPixmap(pixmap_resized)
        self.bitcoin_logo_label.setFixedWidth(logo_label_width)
        self.bitcoin_logo_label.setAlignment(Qt.AlignLeft)

        # create label with etherium logo
        self.etherium_logo_label = QLabel(self)
        pixmap = QPixmap("images/etherium.png")
        pixmap_resized = pixmap.scaledToHeight(logo_height)
        self.etherium_logo_label.setPixmap(pixmap_resized)
        self.etherium_logo_label.setFixedWidth(logo_label_width)
        self.etherium_logo_label.setAlignment(Qt.AlignLeft)

        # create label with litecoin logo
        self.litecoin_logo_label = QLabel(self)
        pixmap = QPixmap("images/litecoin.png")
        pixmap_resized = pixmap.scaledToHeight(logo_height)
        self.litecoin_logo_label.setPixmap(pixmap_resized)
        self.litecoin_logo_label.setFixedWidth(logo_label_width)
        self.litecoin_logo_label.setAlignment(Qt.AlignLeft)

        # create label with dow logo
        self.dow_logo_label = QLabel(self)
        pixmap = QPixmap("images/dow.png")
        pixmap_resized = pixmap.scaledToHeight(logo_height)
        self.dow_logo_label.setPixmap(pixmap_resized)
        self.dow_logo_label.setFixedWidth(logo_label_width)
        self.dow_logo_label.setAlignment(Qt.AlignRight)

        # create label with nasdaq logo
        self.nasdaq_logo_label = QLabel(self)
        pixmap = QPixmap("images/nasdaq.png")
        pixmap_resized = pixmap.scaledToHeight(logo_height)
        self.nasdaq_logo_label.setPixmap(pixmap_resized)
        self.nasdaq_logo_label.setFixedWidth(logo_label_width)
        self.dow_logo_label.setAlignment(Qt.AlignRight)

        # create label with sp500 logo
        self.sp500_logo_label = QLabel(self)
        pixmap = QPixmap("images/sp.png")
        pixmap_resized = pixmap.scaledToHeight(logo_height)
        self.sp500_logo_label.setPixmap(pixmap_resized)
        self.sp500_logo_label.setFixedWidth(logo_label_width)
        self.dow_logo_label.setAlignment(Qt.AlignRight)

        # create bitcoin price label
        self.bitcoin_price_label = QLabel(self)
        bitcoin_price = 69000.32
        self.bitcoin_price_label.setText(f"${round(bitcoin_price):,}")
        self.bitcoin_price_label.setFont(price_font)
        self.bitcoin_price_label.setAlignment(Qt.AlignLeft)

        # create litecoin price label
        self.litecoin_price_label = QLabel(self)
        litecoin_price = 76.32
        self.litecoin_price_label.setText(f"${round(litecoin_price):,}")
        self.litecoin_price_label.setFont(price_font)
        self.litecoin_price_label.setAlignment(Qt.AlignLeft)

        # create etherium price label
        self.etherium_price_label = QLabel(self)
        etherium_price = 3450.36
        self.etherium_price_label.setText(f"${round(etherium_price):,}")
        self.etherium_price_label.setFont(price_font)
        self.etherium_price_label.setAlignment(Qt.AlignLeft)

        # create dow price label
        self.dow_price_label = QLabel(self)
        dow_price = 39700.00
        self.dow_price_label.setText(f"${round(dow_price):,}")
        self.dow_price_label.setFont(price_font)
        self.dow_price_label.setAlignment(Qt.AlignLeft)

        # create nasdaq price label
        self.nasdaq_price_label = QLabel(self)
        nasdaq_price = 16700.36
        self.nasdaq_price_label.setText(f"${round(nasdaq_price):,}")
        self.nasdaq_price_label.setFont(price_font)
        self.nasdaq_price_label.setAlignment(Qt.AlignLeft)

        # create sp500 price label
        self.sp500_price_label = QLabel(self)
        sp500_price = 5340.36
        self.sp500_price_label.setText(f"${round(sp500_price):,}")
        self.sp500_price_label.setFont(price_font)
        self.sp500_price_label.setAlignment(Qt.AlignLeft)

        # set date and time layouts
        self.date_layout.addWidget(self.week_day_label)
        self.date_layout.addWidget(self.date_label)
        self.date_widget = QWidget()
        self.date_widget.setLayout(self.date_layout)

        self.date_time_layout.addWidget(self.time_label)
        self.date_time_layout.addWidget(self.date_widget)
        self.date_time_widget = QWidget()
        self.date_time_widget.setLayout(self.date_time_layout)
        self.date_time_widget.setFixedHeight(clock_label_height)

        # set info layouts
        self.info_layout_1.addWidget(self.bitcoin_logo_label)
        self.info_layout_1.addWidget(self.bitcoin_price_label)
        self.info_layout_1.addWidget(self.dow_logo_label)
        self.info_layout_1.addWidget(self.dow_price_label)

        self.info_layout_2.addWidget(self.etherium_logo_label)
        self.info_layout_2.addWidget(self.etherium_price_label)
        self.info_layout_2.addWidget(self.nasdaq_logo_label)
        self.info_layout_2.addWidget(self.nasdaq_price_label)

        self.info_layout_3.addWidget(self.litecoin_logo_label)
        self.info_layout_3.addWidget(self.litecoin_price_label)
        self.info_layout_3.addWidget(self.sp500_logo_label)
        self.info_layout_3.addWidget(self.sp500_price_label)

        self.info_widget_1 = QWidget()
        self.info_widget_2 = QWidget()
        self.info_widget_3 = QWidget()
        self.info_widget_1.setLayout(self.info_layout_1)
        self.info_widget_2.setLayout(self.info_layout_2)
        self.info_widget_3.setLayout(self.info_layout_3)
        self.info_widget_1.setFixedHeight(info_widget_height)
        self.info_widget_2.setFixedHeight(info_widget_height)
        self.info_widget_3.setFixedHeight(info_widget_height)

        self.setLayout(self.main_layout)

        self.main_layout.addWidget(self.date_time_widget)
        self.main_layout.addWidget(self.info_widget_1)
        self.main_layout.addWidget(self.info_widget_2)
        self.main_layout.addWidget(self.info_widget_3)

        # self.main_layout.addWidget(self.bitcoin_logo_label)
        # self.main_layout.addWidget(self.etherium_logo_label)
        # self.main_layout.addWidget(self.litecoin_logo_label)

        self.setCursor(Qt.BlankCursor)
        self.runDisplay()

    def runDisplay(self):
        self.date_time_timer = QTimer(self)
        self.date_time_timer.timeout.connect(self.updateDateTimeInfo)
        self.date_time_timer.start(1000)  # Update every second

        self.info_data_timer = QTimer(self)
        self.info_data_timer.timeout.connect(self.updateInfoData)
        self.info_data_timer.start(60_000)  # Update every minute

        self.updateDateTimeInfo()
        self.updateInfoData()
        self.resize(800, 480)
        self.setWindowTitle("PyQt5")
        self.show()

    def updateDateTimeInfo(self):
        now = datetime.datetime.now()
        self.time_label.setText(now.strftime("%H:%M"))
        self.date_label.setText(now.strftime("%B %d, %Y"))
        self.week_day_label.setText(now.strftime("%A"))

    def updateCryptoPrices(self):
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        parameters = {"start": "1", "limit": "150", "convert": "USD"}
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "02e9907d-56c4-46c6-a9c7-d14c7af53f6f",
        }

        session = Session()
        session.headers.update(headers)

        response = session.get(url, params=parameters)
        data = json.loads(response.text)

        prices = {}
        for crypto in data["data"]:
            if crypto["name"] == "Bitcoin":
                prices["BTC"] = crypto["quote"]["USD"]["price"]
                prices["BTC-24-CHANGE"] = crypto["quote"]["USD"]["percent_change_24h"]
            elif crypto["name"] == "Ethereum":
                prices["ETH"] = crypto["quote"]["USD"]["price"]
                prices["ETH-24-CHANGE"] = crypto["quote"]["USD"]["percent_change_24h"]
            elif crypto["name"] == "Litecoin":
                prices["LTC"] = crypto["quote"]["USD"]["price"]
                prices["LTC-24-CHANGE"] = crypto["quote"]["USD"]["percent_change_24h"]

        bitcoin_price = round(prices["BTC"])
        litecoin_price = round(prices["LTC"])
        etherium_price = round(prices["ETH"])
        bitcoin_price_change = round(prices["BTC-24-CHANGE"], 2)
        litecoin_price_change = round(prices["LTC-24-CHANGE"], 2)
        etherium_price_change = round(prices["ETH-24-CHANGE"], 2)

        if bitcoin_price_change < 0:
            bitcoin_price_change = bitcoin_price_change * -1
            black_text = f"${bitcoin_price:,} "
            red_text = f"(-{bitcoin_price_change:,}%)"
            total_text = f'{black_text}<span style="color: red;">{red_text}</span'
            self.bitcoin_price_label.setText(total_text)
            self.bitcoin_price_label.setTextFormat(Qt.RichText)
        else:
            black_text = f"${bitcoin_price:,} "
            green_text = f"(+{bitcoin_price_change:,}%)"
            total_text = f'{black_text}<span style="color: green;">{green_text}</span'
            self.bitcoin_price_label.setText(total_text)
            self.bitcoin_price_label.setTextFormat(Qt.RichText)

        if litecoin_price_change < 0:
            litecoin_price_change = litecoin_price_change * -1
            black_text = f"${litecoin_price:,} "
            red_text = f"(-{litecoin_price_change:,}%)"
            total_text = f'{black_text}<span style="color: red;">{red_text}</span'
            self.litecoin_price_label.setText(total_text)
            self.litecoin_price_label.setTextFormat(Qt.RichText)
        else:
            black_text = f"${litecoin_price:,} "
            green_text = f"(+{litecoin_price_change:,}%)"
            total_text = f'{black_text}<span style="color: green;">{green_text}</span'
            self.litecoin_price_label.setText(total_text)
            self.litecoin_price_label.setTextFormat(Qt.RichText)

        if etherium_price_change < 0:
            etherium_price_change = etherium_price_change * -1
            black_text = f"${etherium_price:,} "
            red_text = f"(-{etherium_price_change:,}%)"
            total_text = f'{black_text}<span style="color: red;">{red_text}</span'
            self.etherium_price_label.setText(total_text)
            self.etherium_price_label.setTextFormat(Qt.RichText)
        else:
            black_text = f"${etherium_price:,} "
            green_text = f"(+{etherium_price_change:,}%)"
            total_text = f'{black_text}<span style="color: green;">{green_text}</span'
            self.etherium_price_label.setText(total_text)
            self.etherium_price_label.setTextFormat(Qt.RichText)

    def updateMarketPrices(self):

        indexes = yf.Tickers("^GSPC ^DJI ^IXIC")
        history_sp500 = indexes.tickers["^GSPC"].history(period="1d")
        history_dow = indexes.tickers["^DJI"].history(period="1d")
        history_nasdaq = indexes.tickers["^IXIC"].history(period="1d")

        sp500_current_price = round(history_sp500["Close"].iloc[-1], 2)
        dow_current_price = round(history_dow["Close"].iloc[-1], 2)
        nasdaq_current_price = round(history_nasdaq["Close"].iloc[-1], 2)

        sp500_previous_close = indexes.tickers["^GSPC"].info["previousClose"]
        dow_previous_close = indexes.tickers["^DJI"].info["previousClose"]
        nasdaq_previous_close = indexes.tickers["^IXIC"].info["previousClose"]

        sp500_percentage_change = round(
            ((sp500_current_price - sp500_previous_close) / sp500_previous_close) * 100,
            2,
        )

        dow_percentage_change = round(
            ((dow_current_price - dow_previous_close) / dow_previous_close) * 100,
            2,
        )

        nasdaq_percentage_change = round(
            ((nasdaq_current_price - nasdaq_previous_close) / nasdaq_previous_close)
            * 100,
            2,
        )

        if sp500_percentage_change <= 0:
            black_text = f"${sp500_current_price:,} "
            red_text = f"({sp500_percentage_change:,}%)"
            total_text = f'{black_text}<span style="color: red;">{red_text}</span'
            self.sp500_price_label.setText(total_text)
            self.sp500_price_label.setTextFormat(Qt.RichText)
        else:
            black_text = f"${sp500_current_price:,} "
            green_text = f"({sp500_percentage_change:,}%)"
            total_text = f'{black_text}<span style="color: green;">{green_text}</span'
            self.sp500_price_label.setText(total_text)
            self.sp500_price_label.setTextFormat(Qt.RichText)

        if dow_percentage_change <= 0:
            black_text = f"${dow_current_price:,} "
            red_text = f"({dow_percentage_change:,}%)"
            total_text = f'{black_text}<span style="color: red;">{red_text}</span'
            self.dow_price_label.setText(total_text)
            self.dow_price_label.setTextFormat(Qt.RichText)
        else:
            black_text = f"${dow_current_price:,} "
            green_text = f"({dow_percentage_change:,}%)"
            total_text = f'{black_text}<span style="color: green;">{green_text}</span'
            self.dow_price_label.setText(total_text)
            self.dow_price_label.setTextFormat(Qt.RichText)

        if nasdaq_percentage_change <= 0:
            black_text = f"${nasdaq_current_price:,} "
            red_text = f"({nasdaq_percentage_change:,}%)"
            total_text = f'{black_text}<span style="color: red;">{red_text}</span'
            self.nasdaq_price_label.setText(total_text)
            self.nasdaq_price_label.setTextFormat(Qt.RichText)
        else:
            black_text = f"${nasdaq_current_price:,} "
            green_text = f"({nasdaq_percentage_change:,}%)"
            total_text = f'{black_text}<span style="color: green;">{green_text}</span'
            self.nasdaq_price_label.setText(total_text)
            self.nasdaq_price_label.setTextFormat(Qt.RichText)

    def updateInfoData(self):

        # Get the current time
        current_time = datetime.datetime.now().time()

        # Define the time range
        start_time = datetime.time(0, 0)  # Midnight
        end_time = datetime.time(6, 0)  # 6 AM

        # Check if current time is not between 6 AM and midnight
        if not (start_time <= current_time <= end_time):
            try:
                self.updateCryptoPrices()
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)
                self.bitcoin_price_label.setText("Error!")
                self.litecoin_price_label.setText("Error!")
                self.etherium_price_label.setText("Error!")

            try:
                self.updateMarketPrices()
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)
                self.dow_price_label.setText("Error!")
                self.nasdaq_price_label.setText("Error!")
                self.sp500_price_label.setText("Error!")
            finally:
                pyautogui.moveTo(150, 150)
                pyautogui.click()


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.showFullScreen()  # show fullscreen
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
