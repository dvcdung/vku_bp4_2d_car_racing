from PyQt5 import QtCore, QtGui, QtWidgets
from src.components.play_ai import Ui_frameMapAI
from src.components.play_player import Ui_frameMapPlayer

class Home_ui(object):
    def setupUi(self, frame):
        frame.setObjectName("frame")
        frame.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(frame)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.widget.setStyleSheet("QLabel#label {\n"
"    background-color: #545454;\n"
"    border-radius: 20px;\n"
"}\n"
"QLabel#title_2 {\n"
"    color: #545454;\n"
"}\n"
"QLabel#line {\n"
"    background-color: white;\n"
"}\n"
"QPushButton#nextBtn {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#preBtn {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#playWithHuman {\n"
"    background-color: #545454;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#playWithAI {\n"
"    background-color: #545454;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#playGame {\n"
"    background-color: #d45656;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#playGame:hover {\n"
"    background-color: rgb(214, 48, 49);\n"
"}\n"
"QPushButton#settingBtn {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#playWithHuman:hover {\n"
"    background-color: rgb(99, 110, 114);\n"
"}\n"
"QPushButton#playWithAI:hover {\n"
"    background-color: rgb(99, 110, 114);\n"
"}")
        self.widget.setObjectName("widget")
        self.background = QtWidgets.QLabel(self.widget)
        self.background.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.background.setFont(font)
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/images/home_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(160, 80, 331, 541))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setObjectName("label")
        self.line = QtWidgets.QLabel(self.widget)
        self.line.setGeometry(QtCore.QRect(300, 100, 51, 501))
        self.line.setText("")
        self.line.setObjectName("line")
        self.nextBtn = QtWidgets.QPushButton(self.widget)
        self.nextBtn.setGeometry(QtCore.QRect(490, 320, 70, 70))
        self.nextBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextBtn.setIcon(icon)
        self.nextBtn.setIconSize(QtCore.QSize(60, 60))
        self.nextBtn.setObjectName("nextBtn")
        self.preBtn = QtWidgets.QPushButton(self.widget)
        self.preBtn.setGeometry(QtCore.QRect(95, 320, 70, 70))
        self.preBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.preBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preBtn.setIcon(icon1)
        self.preBtn.setIconSize(QtCore.QSize(70, 70))
        self.preBtn.setObjectName("preBtn")
        self.title_2 = QtWidgets.QLabel(self.widget)
        self.title_2.setGeometry(QtCore.QRect(690, 80, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.title_2.setFont(font)
        self.title_2.setAlignment(QtCore.Qt.AlignCenter)
        self.title_2.setObjectName("title_2")
        self.playWithHuman = QtWidgets.QPushButton(self.widget)
        self.playWithHuman.setGeometry(QtCore.QRect(690, 200, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playWithHuman.setFont(font)
        self.playWithHuman.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playWithHuman.setObjectName("playWithHuman")
        self.playWithAI = QtWidgets.QPushButton(self.widget)
        self.playWithAI.setGeometry(QtCore.QRect(690, 290, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playWithAI.setFont(font)
        self.playWithAI.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playWithAI.setObjectName("playWithAI")
        self.playGame = QtWidgets.QPushButton(self.widget)
        self.playGame.setGeometry(QtCore.QRect(690, 480, 371, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.playGame.setFont(font)
        self.playGame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.playGame.setObjectName("playGame")
        self.car = QtWidgets.QLabel(self.widget)
        self.car.setGeometry(QtCore.QRect(230, 130, 201, 431))
        self.car.setText("")
        self.car.setPixmap(QtGui.QPixmap(":/images/car101.png"))
        self.car.setScaledContents(True)
        self.car.setObjectName("car")
        self.settingBtn = QtWidgets.QPushButton(self.widget)
        self.settingBtn.setGeometry(QtCore.QRect(1130, 10, 60, 60))
        self.settingBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingBtn.setIcon(icon2)
        self.settingBtn.setIconSize(QtCore.QSize(50, 50))
        self.settingBtn.setObjectName("settingBtn")
        frame.setCentralWidget(self.centralwidget)

        self.retranslateUi(frame)
        QtCore.QMetaObject.connectSlotsByName(frame)

    def retranslateUi(self, frame):
        _translate = QtCore.QCoreApplication.translate
        frame.setWindowTitle(_translate("frame", "Racing Game"))
        self.title_2.setText(_translate("frame", "SELECT MODE"))
        self.playWithHuman.setText(_translate("frame", "MULTIPLAYER"))
        self.playWithAI.setText(_translate("frame", "AI"))
        self.playGame.setText(_translate("frame", "PLAY GAME"))