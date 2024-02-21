


from PyQt5 import QtCore, QtGui, QtWidgets
from addFaculty_new import Ui_addFaculty
from removeFaculty import Ui_removeFaculty
from timetableGenerator import Ui_timetable_generator
from send_Notice import Ui_send_notice

class Ui_adminPanel(object):

    def manage_timetable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_timetable_generator()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Manage Timetable function")

    def manage_notice_board(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_send_notice()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Manage notice board function") 

    def open_Add_Faculty(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_addFaculty()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Open Add Faculty Function")

    def open_Remove_Faculty(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_removeFaculty()
        self.ui.setupUi(self.window)
        self.window.show()
        print("Open Remove Faculty Function")

    def setupUi(self, adminPanel):
        adminPanel.setObjectName("adminPanel")
        adminPanel.resize(1114, 842)
        self.centralwidget = QtWidgets.QWidget(adminPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 118, 691, 91))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 240, 1121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ttmanage = QtWidgets.QPushButton(self.centralwidget)
        self.ttmanage.setGeometry(QtCore.QRect(50, 300, 391, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ttmanage.setFont(font)
        self.ttmanage.setObjectName("ttmanage")
        self.ttmanage.clicked.connect(self.manage_timetable)
        self.NBManage = QtWidgets.QPushButton(self.centralwidget)
        self.NBManage.setGeometry(QtCore.QRect(480, 300, 431, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.NBManage.setFont(font)
        self.NBManage.setObjectName("NBManage")
        self.NBManage.clicked.connect(self.manage_notice_board)
        self.addFaculty = QtWidgets.QPushButton(self.centralwidget)
        self.addFaculty.setGeometry(QtCore.QRect(150, 500, 231, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.addFaculty.setFont(font)
        self.addFaculty.setObjectName("addFaculty")
        self.addFaculty.clicked.connect(self.open_Add_Faculty)
        self.removeFaculty = QtWidgets.QPushButton(self.centralwidget)
        self.removeFaculty.setGeometry(QtCore.QRect(450, 500, 311, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.removeFaculty.setFont(font)
        self.removeFaculty.setObjectName("removeFaculty")
        self.removeFaculty.clicked.connect(self.open_Remove_Faculty)
        adminPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(adminPanel)
        QtCore.QMetaObject.connectSlotsByName(adminPanel)

    def retranslateUi(self, adminPanel):
        _translate = QtCore.QCoreApplication.translate
        adminPanel.setWindowTitle(_translate("adminPanel", "MainWindow"))
        self.label.setText(_translate("adminPanel", "Welcome, admin"))
        self.ttmanage.setText(_translate("adminPanel", "Timetable Management"))
        self.NBManage.setText(_translate("adminPanel", "Notice Board Management"))
        self.addFaculty.setText(_translate("adminPanel", "Add Faculty"))
        self.removeFaculty.setText(_translate("adminPanel", "Remove Faculty"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     adminPanel = QtWidgets.QMainWindow()
#     ui = Ui_adminPanel()
#     ui.setupUi(adminPanel)
#     adminPanel.show()
#     sys.exit(app.exec_())
