
from tkinter import messagebox
from PyQt5 import QtCore, QtGui, QtWidgets
from supabase import create_client


class Ui_removeFaculty(object):
    def setupUi(self, removeFaculty):
        removeFaculty.setObjectName("removeFaculty")
        removeFaculty.resize(827, 547)
        self.centralwidget = QtWidgets.QWidget(removeFaculty)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 40, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(220, 170, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 240, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.mail = QtWidgets.QLineEdit(self.centralwidget)
        self.mail.setGeometry(QtCore.QRect(220, 240, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mail.setFont(font)
        self.mail.setObjectName("mail")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 310, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(220, 310, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.removeFromDatabase = QtWidgets.QPushButton(self.centralwidget)
        self.removeFromDatabase.setGeometry(QtCore.QRect(260, 410, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.removeFromDatabase.setFont(font)
        self.removeFromDatabase.setObjectName("removeFromDatabase")
        self.removeFromDatabase.clicked.connect(self.remove_faculty)
        removeFaculty.setCentralWidget(self.centralwidget)

        self.retranslateUi(removeFaculty)
        QtCore.QMetaObject.connectSlotsByName(removeFaculty)

    def retranslateUi(self, removeFaculty):
        _translate = QtCore.QCoreApplication.translate
        removeFaculty.setWindowTitle(_translate("removeFaculty", "Remove Faculty"))
        self.label.setText(_translate("removeFaculty", "Remove Faculty"))
        self.label_3.setText(_translate("removeFaculty", "ID. : "))
        self.label_4.setText(_translate("removeFaculty", "Email : "))
        self.label_7.setText(_translate("removeFaculty", "Password :"))
        self.removeFromDatabase.setText(_translate("removeFaculty", "Remove From Database"))

    def clearUp(self):
        self.id.setText("")
        self.mail.setText("")
        self.password.setText("")

    def remove_faculty(self):
        id = self.id.text()
        mail = self.mail.text()
        password = self.password.text()
        url = "https://ctbocdqgvhimayeqvqov.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0Ym9jZHFndmhpbWF5ZXF2cW92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzNjQ1MzEsImV4cCI6MjAyMTk0MDUzMX0.HHOqs4_KujahCS_V60CsKWjb0ky4UTO2qQNzdyV0sdU"
        supabase = create_client(url, key)
        response = supabase.table('faculty_data').select('mail', 'password').eq("id", id).execute()
        for row in response.data:
            mail_db = row["mail"]
            password_db = row["password"]
        if ((mail == mail_db) and (password == password_db)):
            supabase.table('faculty_data').delete().eq('id', id).execute()
        else : 
            messagebox.critical(None, "Error", "Please Enter appropriare credentials .............")
        self.clearUp()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     removeFaculty = QtWidgets.QMainWindow()
#     ui = Ui_removeFaculty()
#     ui.setupUi(removeFaculty)
#     removeFaculty.show()
#     sys.exit(app.exec_())
