

from PyQt5 import QtCore, QtGui, QtWidgets
from AdminLogin import Ui_AdminLoginPage
from FacultyLogin import Ui_FacultyLoginPage


class Ui_MainWindow(object):

    def openAdminLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AdminLoginPage()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    
    def openFacultyLogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FacultyLoginPage()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1118, 852)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 90, 771, 111))
        font = QtGui.QFont()
        font.setFamily("French Script MT")
        font.setPointSize(35)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 250, 391, 71))
        font = QtGui.QFont()
        font.setFamily("LiSu")
        font.setPointSize(25)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.admin = QtWidgets.QPushButton(self.centralwidget)
        self.admin.setGeometry(QtCore.QRect(290, 430, 231, 171))
        font = QtGui.QFont()
        font.setFamily("Mononoki NF")
        font.setPointSize(15)
        self.admin.setFont(font)
        self.admin.setObjectName("admin")
        self.admin.clicked.connect(self.openAdminLogin)
        self.faculty = QtWidgets.QPushButton(self.centralwidget)
        self.faculty.setGeometry(QtCore.QRect(580, 430, 231, 171))
        font = QtGui.QFont()
        font.setFamily("Mononoki NF")
        font.setPointSize(15)
        self.faculty.setFont(font)
        self.faculty.setObjectName("faculty")
        self.faculty.clicked.connect(self.openFacultyLogin)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timetable & Digital Board Management"))
        self.label.setText(_translate("MainWindow", "Timetable & Digital Board Management"))
        self.label_2.setText(_translate("MainWindow", "Choose Your Role"))
        self.admin.setText(_translate("MainWindow", "ADMIN"))
        self.faculty.setText(_translate("MainWindow", "FACULTY"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
