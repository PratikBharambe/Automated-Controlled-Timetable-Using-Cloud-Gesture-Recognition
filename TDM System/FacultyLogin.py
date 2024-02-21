


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from facultyPanel import Ui_facultyPanel
from supabase import create_client


class Ui_FacultyLoginPage(object):

    def setupUi(self, FacultyLoginPage):
        FacultyLoginPage.setObjectName("FacultyLoginPage")
        FacultyLoginPage.resize(698, 554)
        self.centralwidget = QtWidgets.QWidget(FacultyLoginPage)
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
        FacultyLoginPage.setCentralWidget(self.centralwidget)

        self.retranslateUi(FacultyLoginPage)
        QtCore.QMetaObject.connectSlotsByName(FacultyLoginPage)

    def retranslateUi(self, FacultyLoginPage):
        _translate = QtCore.QCoreApplication.translate
        FacultyLoginPage.setWindowTitle(_translate("FacultyLoginPage", "MainWindow"))
        self.label.setText(_translate("FacultyLoginPage", "Faculty Login"))
        self.label_2.setText(_translate("FacultyLoginPage", "Login ID : "))
        self.label_3.setText(_translate("FacultyLoginPage", "Password : "))
        self.loginButton.setText(_translate("FacultyLoginPage", "Login"))

    def openFacultyPanel(self, faculty_name):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_facultyPanel()
        self.ui.setupUi(self.window)
        self.ui.update_faculty_name(faculty_name)
        self.window.show()

    def checkCredentials(self):
        url = "https://ctbocdqgvhimayeqvqov.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0Ym9jZHFndmhpbWF5ZXF2cW92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzNjQ1MzEsImV4cCI6MjAyMTk0MDUzMX0.HHOqs4_KujahCS_V60CsKWjb0ky4UTO2qQNzdyV0sdU"
        supabase = create_client(url, key)
        id = self.loginID.text()
        password = self.password.text()
        try:
            ressponse = supabase.table("faculty_data").select("password", "name").eq("mail", id).execute()
            for entry_key in ressponse.data:
                database_password = entry_key["password"]
                facultyName = entry_key["name"]
            if (password == database_password):
                self.openFacultyPanel(facultyName)
        except: 
            QMessageBox.critical(None, "Error", "Please check entered credentials .............")


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     FacultyLoginPage = QtWidgets.QMainWindow()
#     ui = Ui_FacultyLoginPage()
#     ui.setupUi(FacultyLoginPage)
#     FacultyLoginPage.show()
#     sys.exit(app.exec_())
