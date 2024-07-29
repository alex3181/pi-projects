import sys
import datetime


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
        time_font.setPointSize(55)
        time_font.bold()

        crypto_price_font = QFont()
        crypto_price_font.setFamily(font_family)
        crypto_price_font.setPointSize(30)
        crypto_price_font.bold()

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.setWindowFlag(Qt.FramelessWindowHint)

        # Set up a main Layout. It will be vertical
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # Set up a date and time Layout. It will be horizontal
        self.date_time_layout = QHBoxLayout()

        # Set up a date Layout. It will be vertical
        self.date_layout = QVBoxLayout()

        # Set up 3 information layouts. They will be horizontal
        self.info_layout_1 = QHBoxLayout()
        self.info_layout_1.setContentsMargins(15, 0, 15, 0)
        self.info_layout_2 = QHBoxLayout()
        self.info_layout_2.setContentsMargins(15, 0, 15, 0)
        self.info_layout_3 = QHBoxLayout()
        self.info_layout_3.setContentsMargins(15, 0, 15, 0)

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

        max_gap = 5
        crypto_logo_height = 55
        crypto_logo_label_width = 70
        info_widget_height = 55
        clock_label_height = 170

        # create gap2 label
        self.gap1 = Color("black")
        self.gap1.setMaximumWidth(max_gap)

        # create gap2 label
        self.gap2 = Color("black")
        self.gap2.setMaximumHeight(max_gap)

        # create label with bitcoin logo
        self.bitcoin_logo_label = QLabel(self)
        pixmap = QPixmap("images/bitcoin.png")
        pixmap_resized = pixmap.scaledToHeight(crypto_logo_height)
        self.bitcoin_logo_label.setPixmap(pixmap_resized)
        self.bitcoin_logo_label.setFixedWidth(crypto_logo_label_width)

        # create label with etherium logo
        self.etherium_logo_label = QLabel(self)
        pixmap = QPixmap("images/etherium.png")
        pixmap_resized = pixmap.scaledToHeight(crypto_logo_height)
        self.etherium_logo_label.setPixmap(pixmap_resized)
        self.etherium_logo_label.setFixedWidth(crypto_logo_label_width)

        # create label with litecoin logo
        self.litecoin_logo_label = QLabel(self)
        pixmap = QPixmap("images/litecoin.png")
        pixmap_resized = pixmap.scaledToHeight(crypto_logo_height)
        self.litecoin_logo_label.setPixmap(pixmap_resized)
        self.litecoin_logo_label.setFixedWidth(crypto_logo_label_width)

        # create bitcoin price label
        self.bitcoin_price_label = QLabel(self)
        bitcoin_price = 69000.32
        self.bitcoin_price_label.setText(f"${round(bitcoin_price):,}")
        self.bitcoin_price_label.setFont(crypto_price_font)
        self.bitcoin_price_label.setAlignment(Qt.AlignmentFlag.AlignLeft)

        # create litecoin price label
        self.litecoin_price_label = QLabel(self)
        litecoin_price = 76.32
        self.litecoin_price_label.setText(f"${round(litecoin_price):,}")
        self.litecoin_price_label.setFont(crypto_price_font)

        # create litecoin price label
        self.etherium_price_label = QLabel(self)
        etherium_price = 3450.36
        self.etherium_price_label.setText(f"${round(etherium_price):,}")
        self.etherium_price_label.setFont(crypto_price_font)

        # set date and time layouts
        self.date_layout.addWidget(self.week_day_label)
        self.date_layout.addWidget(self.date_label)
        self.date_widget = QWidget()
        self.date_widget.setLayout(self.date_layout)

        self.date_time_layout.addWidget(self.time_label)
        self.date_time_layout.addWidget(self.gap1)
        self.date_time_layout.addWidget(self.date_widget)
        self.date_time_widget = QWidget()
        self.date_time_widget.setLayout(self.date_time_layout)
        self.date_time_widget.setFixedHeight(clock_label_height)

        # set info layouts
        self.info_layout_1.addWidget(self.bitcoin_logo_label)
        self.info_layout_1.addWidget(self.bitcoin_price_label)

        self.info_layout_2.addWidget(self.etherium_logo_label)
        self.info_layout_2.addWidget(self.etherium_price_label)

        self.info_layout_3.addWidget(self.litecoin_logo_label)
        self.info_layout_3.addWidget(self.litecoin_price_label)
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
        self.main_layout.addWidget(self.gap2)
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

    def updateInfoData(self):

        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
        parameters = {"start": "1", "limit": "150", "convert": "USD"}
        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": "02e9907d-56c4-46c6-a9c7-d14c7af53f6f",
        }

        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            price_BTC = data["data"][0]["quote"]["USD"]["price"]
            price_ETH = data["data"][1]["quote"]["USD"]["price"]
            # print(f"${price:,.2f}")
            prices = {}
            for crypto in data["data"]:
                if crypto["name"] == "Bitcoin":
                    prices["BTC"] = crypto["quote"]["USD"]["price"]
                elif crypto["name"] == "Ethereum":
                    prices["ETH"] = crypto["quote"]["USD"]["price"]
                elif crypto["name"] == "Litecoin":
                    prices["LTC"] = crypto["quote"]["USD"]["price"]
            bitcoin_price = round(prices["BTC"])
            litecoin_price = round(prices["LTC"])
            etherium_price = round(prices["ETH"])
            self.bitcoin_price_label.setText(f"${bitcoin_price:,}")
            self.litecoin_price_label.setText(f"${litecoin_price:,}")
            self.etherium_price_label.setText(f"${etherium_price:,}")

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            self.bitcoin_price_label.setText("Error!")
            self.litecoin_price_label.setText("Error!")
            self.etherium_price_label.setText("Error!")


def main():
    app = QApplication(sys.argv)
    ex = window()
    ex.showFullScreen()  # show fullscreen
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
