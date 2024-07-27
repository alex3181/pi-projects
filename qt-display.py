import sys
import datetime

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

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        # self.setWindowFlag(Qt.FramelessWindowHint)

        # Set up a main Layout. It will be vertical
        self.mainLayout = QVBoxLayout()
        # self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set up a date and time Layout. It will be horizontal
        self.dateTimeLayout = QHBoxLayout()
        # self.dateTimeLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Set up a date Layout. It will be vertical
        self.dateLayout = QVBoxLayout()
        # self.dateLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        # create gap2 label
        self.gap1 = Color("black")
        self.gap1.setMaximumWidth(max_gap)

        # create gap2 label
        self.gap2 = Color("black")
        self.gap2.setMaximumHeight(max_gap)

        crypto_logo_height = 50
        info_label_height = 75
        clock_label_height = 150

        # create label with bitcoin logo
        self.bitcoin_logo_label = QLabel(self)
        pixmap = QPixmap("images/bitcoin.png")
        pixmap_resized = pixmap.scaledToHeight(crypto_logo_height)
        self.bitcoin_logo_label.setPixmap(pixmap_resized)
        self.bitcoin_logo_label.setFixedHeight(info_label_height)
        # self.bitcoin_logo_label.setText = "Bitcoin"

        # create label with etherium logo
        self.etherium_logo_label = QLabel(self)
        pixmap = QPixmap("images/etherium.png")
        pixmap_resized = pixmap.scaledToHeight(crypto_logo_height)
        self.etherium_logo_label.setPixmap(pixmap_resized)
        self.etherium_logo_label.setFixedHeight(info_label_height)
        # self.etherium_logo_label.setText = "etherium"

        # create label with litecoin logo
        self.litecoin_logo_label = QLabel(self)
        pixmap = QPixmap("images/litecoin.png")
        pixmap_resized = pixmap.scaledToHeight(crypto_logo_height)
        self.litecoin_logo_label.setPixmap(pixmap_resized)
        self.litecoin_logo_label.setFixedHeight(info_label_height)
        # self.litecoin_logo_label.setText = "litecoin_logo_label"

        # set up layouts
        self.dateLayout.addWidget(self.week_day_label)
        self.dateLayout.addWidget(self.date_label)
        self.date_widget = QWidget()
        self.date_widget.setLayout(self.dateLayout)

        self.dateTimeLayout.addWidget(self.time_label)
        self.dateTimeLayout.addWidget(self.gap1)
        self.dateTimeLayout.addWidget(self.date_widget)
        self.date_time_widget = QWidget()
        self.date_time_widget.setLayout(self.dateTimeLayout)
        self.date_time_widget.setFixedHeight(clock_label_height)

        self.setLayout(self.mainLayout)
        self.mainLayout.addWidget(self.date_time_widget)
        self.mainLayout.addWidget(self.gap2)

        # self.mainLayout.addWidget(Color("red"))
        self.mainLayout.addWidget(self.bitcoin_logo_label)
        self.mainLayout.addWidget(self.etherium_logo_label)
        self.mainLayout.addWidget(self.litecoin_logo_label)
        # self.mainLayout.addWidget(Color("green"))

        self.setCursor(Qt.BlankCursor)
        self.runDisplay()

    def runDisplay(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateInfo)
        self.timer.start(1000)  # Update every second
        self.updateInfo()
        self.resize(800, 480)
        self.setWindowTitle("PyQt5")
        self.show()

    def updateInfo(self):
        now = datetime.datetime.now()
        self.time_label.setText(now.strftime("%H:%M"))
        self.date_label.setText(now.strftime("%B %d, %Y"))
        self.week_day_label.setText(now.strftime("%A"))


def main():
    app = QApplication(sys.argv)
    ex = window()
    # ex.showFullScreen()  # show fullscreen
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
