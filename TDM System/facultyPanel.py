from PyQt5 import QtCore, QtGui, QtWidgets
from be_tt_display import Ui_be_tt_display
from send_Notice import Ui_send_notice
import reschedule_lecture


class Ui_facultyPanel(object):

    def open_bt_timtable(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_be_tt_display()
        self.ui.setupUi(self.window)
        self.window.show()

    def open_send_notice(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_send_notice()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, facultyPanel):
        facultyPanel.setObjectName("facultyPanel")
        facultyPanel.resize(1114, 840)
        self.centralwidget = QtWidgets.QWidget(facultyPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 120, 211, 101))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Relec = QtWidgets.QPushButton(self.centralwidget)
        self.Relec.setGeometry(QtCore.QRect(320, 530, 351, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Relec.setFont(font)
        self.Relec.setObjectName("Relec")
        self.Relec.clicked.connect(self.reshedule_lecture)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-10, 250, 1121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ttmanage = QtWidgets.QPushButton(self.centralwidget)
        self.ttmanage.setGeometry(QtCore.QRect(40, 330, 391, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ttmanage.setFont(font)
        self.ttmanage.setObjectName("ttmanage")
        self.ttmanage.clicked.connect(self.open_bt_timtable)
        self.NBManage = QtWidgets.QPushButton(self.centralwidget)
        self.NBManage.setGeometry(QtCore.QRect(470, 330, 431, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.NBManage.setFont(font)
        self.NBManage.setObjectName("NBManage")
        self.NBManage.clicked.connect(self.open_send_notice)
        self.faculty_name = QtWidgets.QLabel(self.centralwidget)
        self.faculty_name.setGeometry(QtCore.QRect(270, 120, 551, 101))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(25)
        self.faculty_name.setFont(font)
        self.faculty_name.setText("")
        self.faculty_name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.faculty_name.setObjectName("faculty_name")
        facultyPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(facultyPanel)
        QtCore.QMetaObject.connectSlotsByName(facultyPanel)

    def retranslateUi(self, facultyPanel):
        _translate = QtCore.QCoreApplication.translate
        facultyPanel.setWindowTitle(_translate("facultyPanel", "MainWindow"))
        self.label.setText(_translate("facultyPanel", "Welcome,"))
        self.Relec.setText(_translate("facultyPanel", "Reschedule Lecture"))
        self.ttmanage.setText(_translate("facultyPanel", "View Timetable"))
        self.NBManage.setText(_translate("facultyPanel", "Notice Board Management"))

    def update_faculty_name(self, name):
        self.faculty_name.setText(name)
        self.fac_name = name

    def reshedule_lecture(self):
        reschedule_lecture.initialize_reshedule_algorithm(self.fac_name)

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     facultyPanel = QtWidgets.QMainWindow()
#     ui = Ui_facultyPanel()
#     ui.setupUi(facultyPanel)
#     facultyPanel.show()
#     sys.exit(app.exec_())
