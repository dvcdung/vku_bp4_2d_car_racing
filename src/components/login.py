from PyQt5 import QtCore, QtGui, QtWidgets
import src.components.res_rc as res_rc
from game_server.database import DB

db = DB()
user_data = {}

class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 650)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 600, 650))
        self.widget.setStyleSheet("QPushButton#loginTab, #registerTab {\n"
"    background-color: rgb(165, 177, 194);\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: #000;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QWidget#widget {\n"
"    background-color: rgb(0, 206, 201);\n"
"}\n"
"QLineEdit#username, #passText, #usernameRe, #displayName, #passTextRepeat {\n"
"    border-radius: 12px;\n"
"    padding: 0px 0px 5px 10px;\n"
"    border-bottom: 1px solid #545454;\n"
"}\n"
"QPushButton#loginBtn {\n"
"    background-color: #d45656;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: #fff;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}\n"
"QPushButton#registerBtn {\n"
"    background-color: rgb(32, 191, 107);\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"      color: #fff;\n"
"    text-align: center;\n"
"    padding-bottom: 5px;\n"
"}")
        self.widget.setObjectName("widget")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 601, 81))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.loginTab = QtWidgets.QPushButton(self.frame)
        self.loginTab.setGeometry(QtCore.QRect(10, 10, 285, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.loginTab.setFont(font)
        self.loginTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/enter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginTab.setIcon(icon)
        self.loginTab.setIconSize(QtCore.QSize(25, 25))
        self.loginTab.setObjectName("loginTab")
        self.registerTab = QtWidgets.QPushButton(self.frame)
        self.registerTab.setGeometry(QtCore.QRect(305, 10, 285, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.registerTab.setFont(font)
        self.registerTab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.registerTab.setIcon(icon1)
        self.registerTab.setIconSize(QtCore.QSize(25, 25))
        self.registerTab.setAutoRepeat(False)
        self.registerTab.setObjectName("registerTab")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 89, 601, 561))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageLogin = QtWidgets.QWidget()
        self.pageLogin.setObjectName("pageLogin")
        self.label = QtWidgets.QLabel(self.pageLogin)
        self.label.setGeometry(QtCore.QRect(220, 10, 160, 160))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/images/user_1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.pageLogin)
        self.label_2.setGeometry(QtCore.QRect(200, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.username = QtWidgets.QLineEdit(self.pageLogin)
        self.username.setGeometry(QtCore.QRect(140, 250, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username.setObjectName("username")
        self.passText = QtWidgets.QLineEdit(self.pageLogin)
        self.passText.setGeometry(QtCore.QRect(140, 330, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.passText.setFont(font)
        self.passText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passText.setObjectName("passText")
        self.loginBtn = QtWidgets.QPushButton(self.pageLogin)
        self.loginBtn.setGeometry(QtCore.QRect(140, 440, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.loginBtn.setFont(font)
        self.loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.loginBtn.setObjectName("loginBtn")
        self.stackedWidget.addWidget(self.pageLogin)
        self.pageRegister = QtWidgets.QWidget()
        self.pageRegister.setObjectName("pageRegister")
        self.label_3 = QtWidgets.QLabel(self.pageRegister)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 160, 160))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/images/register.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.pageRegister)
        self.label_4.setGeometry(QtCore.QRect(200, 170, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.usernameRe = QtWidgets.QLineEdit(self.pageRegister)
        self.usernameRe.setGeometry(QtCore.QRect(140, 240, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.usernameRe.setFont(font)
        self.usernameRe.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.usernameRe.setObjectName("usernameRe")
        self.displayName = QtWidgets.QLineEdit(self.pageRegister)
        self.displayName.setGeometry(QtCore.QRect(140, 320, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.displayName.setFont(font)
        self.displayName.setObjectName("displayName")
        self.passTextRepeat = QtWidgets.QLineEdit(self.pageRegister)
        self.passTextRepeat.setGeometry(QtCore.QRect(140, 400, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.passTextRepeat.setFont(font)
        self.passTextRepeat.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passTextRepeat.setObjectName("passTextRepeat")
        self.registerBtn = QtWidgets.QPushButton(self.pageRegister)
        self.registerBtn.setGeometry(QtCore.QRect(140, 480, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.registerBtn.setFont(font)
        self.registerBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registerBtn.setObjectName("registerBtn")
        self.stackedWidget.addWidget(self.pageRegister)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.loginTab.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageLogin))
        self.registerTab.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegister))
        self.loginBtn.clicked.connect(self.login)
        self.registerBtn.clicked.connect(self.register)

    def login(self):
        username = self.username.text()
        password = self.passText.text()
        user = db.getUser(username, password)
        if user and len(user) == 1:
            print("Login ok")

    def register(self):
        usernameRe = self.usernameRe.text()
        displayName = self.displayName.text()
        passwordRe = self.passTextRepeat.text()
        userRe = db.insertUser((usernameRe, passwordRe, displayName))
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.loginTab.setText(_translate("MainWindow", " LOGIN"))
        self.registerTab.setText(_translate("MainWindow", " REGISTER"))
        self.label_2.setText(_translate("MainWindow", "LOGIN"))
        self.username.setPlaceholderText(_translate("MainWindow", "Enter the username"))
        self.passText.setPlaceholderText(_translate("MainWindow", "Enter the password"))
        self.loginBtn.setText(_translate("MainWindow", "LOGIN"))
        self.label_4.setText(_translate("MainWindow", "REGISTER"))
        self.usernameRe.setPlaceholderText(_translate("MainWindow", "Enter the username"))
        self.displayName.setPlaceholderText(_translate("MainWindow", "Enter the display name"))
        self.passTextRepeat.setPlaceholderText(_translate("MainWindow", "Enter the password"))
        self.registerBtn.setText(_translate("MainWindow", "REGISTER"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
