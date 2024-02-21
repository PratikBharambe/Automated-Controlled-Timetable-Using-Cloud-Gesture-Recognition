


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from adminPanel import Ui_adminPanel

class Ui_AdminLoginPage(object):

    def setupUi(self, AdminLoginPage):
        AdminLoginPage.setObjectName("AdminLoginPage")
        AdminLoginPage.resize(698, 554)
        self.centralwidget = QtWidgets.QWidget(AdminLoginPage)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 70, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Informal Roman")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.loginID = QtWidgets.QLineEdit(self.centralwidget)
        self.loginID.setGeometry(QtCore.QRect(260, 190, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.loginID.setFont(font)
        self.loginID.setObjectName("loginID")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(260, 260, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 190, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 260, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(250, 340, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setItalic(True)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.clicked.connect(self.checkCredentials)
        AdminLoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminLoginPage)
        QtCore.QMetaObject.connectSlotsByName(AdminLoginPage)

    def retranslateUi(self, AdminLoginPage):
        _translate = QtCore.QCoreApplication.translate
        AdminLoginPage.setWindowTitle(_translate("AdminLoginPage", "MainWindow"))
        self.label.setText(_translate("AdminLoginPage", "Admin Login"))
        self.label_2.setText(_translate("AdminLoginPage", "Login ID : "))
        self.label_3.setText(_translate("AdminLoginPage", "Password : "))
        self.loginButton.setText(_translate("AdminLoginPage", "Login"))

    
    def openAdminPanel(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_adminPanel()
        self.ui.setupUi(self.window)
        self.window.show()

    def checkCredentials(self):
        print("Login Button Pressed ...........")
        id = self.loginID.text()
        password = self.password.text()
        if ((id == "admin@gmail.com") and (password == "password")):
            self.openAdminPanel()
        else : 
            QMessageBox.critical(None, "Error", "Please Enter appropriare credentials .............")

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AdminLoginPage = QtWidgets.QMainWindow()
#     ui = Ui_AdminLoginPage()
#     ui.setupUi(AdminLoginPage)
#     AdminLoginPage.show()
#     sys.exit(app.exec_())
