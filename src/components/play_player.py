from PyQt5 import QtCore, QtGui, QtWidgets
import src.components.res_rc as res_rc

class Ui_frameMapPlayer(object):
    def setupUi(self, frameMapPlayer):
        frameMapPlayer.setObjectName("frameMapPlayer")
        frameMapPlayer.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(frameMapPlayer)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.widget.setStyleSheet("QPushButton#backBtn, #nextBtn, #preBtn, #backBtn {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#startBtn {\n"
"    background-color: #d45656;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#loginBtn {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/home_background.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.backBtn = QtWidgets.QPushButton(self.widget)
        self.backBtn.clicked.connect(frameMapPlayer.close)
        self.backBtn.setGeometry(QtCore.QRect(20, 10, 60, 60))
        self.backBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/back_to.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.backBtn.setIcon(icon)
        self.backBtn.setIconSize(QtCore.QSize(50, 50))
        self.backBtn.setObjectName("backBtn")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(490, 60, 251, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.listMap = QtWidgets.QLabel(self.widget)
        self.listMap.setGeometry(QtCore.QRect(360, 130, 500, 300))
        self.listMap.setText("")
        self.listMap.setPixmap(QtGui.QPixmap(":/images/map01.png"))
        self.listMap.setScaledContents(True)
        self.listMap.setObjectName("listMap")
        self.preBtn = QtWidgets.QPushButton(self.widget)
        self.preBtn.setGeometry(QtCore.QRect(305, 250, 60, 60))
        self.preBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.preBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/left-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.preBtn.setIcon(icon1)
        self.preBtn.setIconSize(QtCore.QSize(60, 60))
        self.preBtn.setObjectName("preBtn")
        self.nextBtn = QtWidgets.QPushButton(self.widget)
        self.nextBtn.setGeometry(QtCore.QRect(860, 250, 60, 60))
        self.nextBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextBtn.setIcon(icon2)
        self.nextBtn.setIconSize(QtCore.QSize(50, 50))
        self.nextBtn.setObjectName("nextBtn")
        self.startBtn = QtWidgets.QPushButton(self.widget)
        self.startBtn.setGeometry(QtCore.QRect(450, 510, 331, 81))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startBtn.setObjectName("startBtn")
        self.loginBtn = QtWidgets.QPushButton(self.widget)
        self.loginBtn.setGeometry(QtCore.QRect(1130, 10, 60, 60))
        self.loginBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginBtn.setIcon(icon3)
        self.loginBtn.setIconSize(QtCore.QSize(60, 60))
        self.loginBtn.setObjectName("loginBtn")
        frameMapPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(frameMapPlayer)
        QtCore.QMetaObject.connectSlotsByName(frameMapPlayer)

    def retranslateUi(self, frameMapPlayer):
        _translate = QtCore.QCoreApplication.translate
        frameMapPlayer.setWindowTitle(_translate("frameMapPlayer", "MainWindow"))
        self.label_2.setText(_translate("frameMapPlayer", "SELECT MAP"))
        self.startBtn.setText(_translate("frameMapPlayer", "Start"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frameMapPlayer = QtWidgets.QMainWindow()
    ui = Ui_frameMapPlayer()
    ui.setupUi(frameMapPlayer)
    frameMapPlayer.show()
    sys.exit(app.exec_())
