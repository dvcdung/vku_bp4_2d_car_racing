from PyQt5 import QtCore, QtGui, QtWidgets
import src.components.res_rc as res_rc

class Ui_frameMapAI(object):
    def setupUi(self, frameMapAI):
        frameMapAI.setObjectName("frameMapAI")
        frameMapAI.resize(1200, 700)
        self.centralwidget = QtWidgets.QWidget(frameMapAI)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.widget.setStyleSheet("QPushButton#backBtn, #nextBtn, #preBtn {\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton#easyMode {\n"
"    background-color: #545454;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#mediumMode {\n"
"    background-color: #545454;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#hardMode {\n"
"    background-color: #545454;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#startBtn {\n"
"    background-color: #d45656;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: white;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#startBtn:hover {\n"
"    background-color: rgb(214, 48, 49);\n"
"}\n"
"QPushButton#easyMode:hover {\n"
"    background-color: rgb(99, 110, 114);\n"
"}\n"
"QPushButton#hardMode:hover {\n"
"    background-color: rgb(99, 110, 114);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1200, 700))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/back_ground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.backBtn = QtWidgets.QPushButton(self.widget)
        self.backBtn.clicked.connect(frameMapAI.close)
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
        self.easyMode = QtWidgets.QPushButton(self.widget)
        self.easyMode.setGeometry(QtCore.QRect(320, 460, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.easyMode.setFont(font)
        self.easyMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.easyMode.setObjectName("easyMode")
        self.hardMode = QtWidgets.QPushButton(self.widget)
        self.hardMode.setGeometry(QtCore.QRect(630, 460, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.hardMode.setFont(font)
        self.hardMode.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hardMode.setObjectName("hardMode")
        self.startBtn = QtWidgets.QPushButton(self.widget)
        self.startBtn.setGeometry(QtCore.QRect(460, 560, 301, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.startBtn.setFont(font)
        self.startBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startBtn.setObjectName("startBtn")
        frameMapAI.setCentralWidget(self.centralwidget)

        self.retranslateUi(frameMapAI)
        QtCore.QMetaObject.connectSlotsByName(frameMapAI)
        
    def retranslateUi(self, frameMapAI):
        _translate = QtCore.QCoreApplication.translate
        frameMapAI.setWindowTitle(_translate("frameMapAI", "MainWindow"))
        self.label_2.setText(_translate("frameMapAI", "SELECT MAP"))
        self.easyMode.setText(_translate("frameMapAI", "Easy"))
        self.hardMode.setText(_translate("frameMapAI", "Hard"))
        self.startBtn.setText(_translate("frameMapAI", "Start"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    frameMapAI = QtWidgets.QMainWindow()
    ui = Ui_frameMapAI()
    ui.setupUi(frameMapAI)
    frameMapAI.show()
    sys.exit(app.exec_())
