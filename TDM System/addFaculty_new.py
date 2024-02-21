# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addFaculty.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from supabase import create_client


class Ui_addFaculty(object):
    def setupUi(self, addFaculty):
        addFaculty.setObjectName("addFaculty")
        addFaculty.resize(1144, 841)
        self.centralwidget = QtWidgets.QWidget(addFaculty)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 50, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 190, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(400, 190, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 260, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.id = QtWidgets.QLineEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(400, 260, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.id.setFont(font)
        self.id.setObjectName("id")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 330, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.mail = QtWidgets.QLineEdit(self.centralwidget)
        self.mail.setGeometry(QtCore.QRect(400, 330, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mail.setFont(font)
        self.mail.setObjectName("mail")
        self.mobile = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile.setGeometry(QtCore.QRect(400, 470, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mobile.setFont(font)
        self.mobile.setObjectName("mobile")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 540, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(250, 470, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 400, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(400, 400, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.AddToDatabase = QtWidgets.QPushButton(self.centralwidget)
        self.AddToDatabase.setGeometry(QtCore.QRect(440, 700, 291, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.AddToDatabase.setFont(font)
        self.AddToDatabase.setObjectName("AddToDatabase")
        self.AddToDatabase.clicked.connect(self.send_Data)
        self.textToUpdate = QtWidgets.QLabel(self.centralwidget)
        self.textToUpdate.setGeometry(QtCore.QRect(220, 730, 721, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.textToUpdate.setFont(font)
        self.textToUpdate.setText("")
        self.textToUpdate.setAlignment(QtCore.Qt.AlignCenter)
        self.textToUpdate.setObjectName("textToUpdate")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 610, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.subject = QtWidgets.QComboBox(self.centralwidget)
        self.subject.setGeometry(QtCore.QRect(400, 610, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.subject.setFont(font)
        self.subject.setObjectName("subject")
        self.subject.addItem("")
        self.subject.addItem("")
        self.subject.addItem("")
        self.subject.addItem("")
        self.subject.addItem("")
        self.subject.addItem("")
        self.subject.addItem("")
        self.gender = QtWidgets.QComboBox(self.centralwidget)
        self.gender.setGeometry(QtCore.QRect(400, 540, 521, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.gender.setFont(font)
        self.gender.setObjectName("gender")
        self.gender.addItem("")
        self.gender.addItem("")
        addFaculty.setCentralWidget(self.centralwidget)

        self.retranslateUi(addFaculty)
        QtCore.QMetaObject.connectSlotsByName(addFaculty)

    def retranslateUi(self, addFaculty):
        _translate = QtCore.QCoreApplication.translate
        addFaculty.setWindowTitle(_translate("addFaculty", "MainWindow"))
        self.label.setText(_translate("addFaculty", "Add Faculty"))
        self.label_2.setText(_translate("addFaculty", "Name : "))
        self.label_3.setText(_translate("addFaculty", "ID. : "))
        self.label_4.setText(_translate("addFaculty", "Email : "))
        self.label_5.setText(_translate("addFaculty", "Gender : "))
        self.label_6.setText(_translate("addFaculty", "Phone No. : "))
        self.label_7.setText(_translate("addFaculty", "Password :"))
        self.AddToDatabase.setText(_translate("addFaculty", "Add To Database"))
        self.label_8.setText(_translate("addFaculty", "Subject : "))
        self.subject.setItemText(0, _translate("addFaculty", "FOC"))
        self.subject.setItemText(1, _translate("addFaculty", "MC"))
        self.subject.setItemText(2, _translate("addFaculty", "DM"))
        self.subject.setItemText(3, _translate("addFaculty", "DBM"))
        self.subject.setItemText(4, _translate("addFaculty", "I&E"))
        self.subject.setItemText(5, _translate("addFaculty", "PROJECT"))
        self.subject.setItemText(6, _translate("addFaculty", "HONOURS"))
        self.gender.setItemText(0, _translate("addFaculty", "Male"))
        self.gender.setItemText(1, _translate("addFaculty", "Female"))

    def clearUp(self):
        self.name.setText("")
        self.id.setText("")
        self.mail.setText("")
        self.mobile.setText("")
        self.password.setText("")
        

    def send_Data(self):
        name = self.name.text()
        id = int(self.id.text())
        mail = self.mail.text()
        mobile = int(self.mobile.text())
        password = self.password.text()
        gender = self.gender.currentText()
        subject = self.subject.currentText()
        url = "https://ctbocdqgvhimayeqvqov.supabase.co"
        key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0Ym9jZHFndmhpbWF5ZXF2cW92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzNjQ1MzEsImV4cCI6MjAyMTk0MDUzMX0.HHOqs4_KujahCS_V60CsKWjb0ky4UTO2qQNzdyV0sdU"
        supabase = create_client(url, key)
        supabase.table('faculty_data').insert({"id" : id, "name" : name, "mail" : mail, "mobile" : mobile, "password" : password, "gender" : gender, "subject" : subject}).execute()
        self.clearUp()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     addFaculty = QtWidgets.QMainWindow()
#     ui = Ui_addFaculty()
#     ui.setupUi(addFaculty)
#     addFaculty.show()
#     sys.exit(app.exec_())