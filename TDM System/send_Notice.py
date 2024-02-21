

from PyQt5 import QtCore, QtGui, QtWidgets
from supabase import create_client



class Ui_send_notice(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1199, 904)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 881, 151))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(48)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 170, 1011, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 280, 681, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 390, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.SendButton = QtWidgets.QPushButton(self.centralwidget)
        self.SendButton.setGeometry(QtCore.QRect(330, 610, 571, 101))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setItalic(True)
        self.SendButton.setFont(font)
        self.SendButton.setObjectName("SendButton")
        self.MessageToUpdate = QtWidgets.QLabel(self.centralwidget)
        self.MessageToUpdate.setGeometry(QtCore.QRect(130, 740, 1001, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setItalic(True)
        self.MessageToUpdate.setFont(font)
        self.MessageToUpdate.setText("")
        self.MessageToUpdate.setAlignment(QtCore.Qt.AlignCenter)
        self.MessageToUpdate.setObjectName("MessageToUpdate")
        self.noticeToSend = QtWidgets.QTextEdit(self.centralwidget)
        self.noticeToSend.setGeometry(QtCore.QRect(410, 400, 661, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setItalic(True)
        self.noticeToSend.setFont(font)
        self.noticeToSend.setObjectName("noticeToSend")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1199, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Digital Notice Board"))
        self.label.setText(_translate("MainWindow", "Digital Notice Board"))
        self.label_2.setText(_translate("MainWindow", "RMD Sinhgad School Of Engineering, Warje, Pune"))
        self.label_3.setText(_translate("MainWindow", "Department Of Electronics And Telecommunication"))
        self.label_4.setText(_translate("MainWindow", "Enter Notice To Display : "))
        self.SendButton.setText(_translate("MainWindow", "Send And Display"))

        self.SendButton.clicked.connect(self.getAndSendNotice)

    def getAndSendNotice(self):
        notice = self.noticeToSend.toPlainText()
        isSent = self.sendTextMessage(notice)
        if isSent == True:
            self.MessageToUpdate.setText("Notice updated Successfully !!!!!")
        else :
            self.MessageToUpdate.setText("Not Updated please check Internet connection !!!!!")


    def sendTextMessage(self, message):
        try:
            url = "https://ctbocdqgvhimayeqvqov.supabase.co"
            key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImN0Ym9jZHFndmhpbWF5ZXF2cW92Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDYzNjQ1MzEsImV4cCI6MjAyMTk0MDUzMX0.HHOqs4_KujahCS_V60CsKWjb0ky4UTO2qQNzdyV0sdU"
            supabase = create_client(url, key)
            supabase.table('notice_board').update({'notice': f'{message}'}).eq('id', 1).execute()
            return True
        except:
            return False


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_send_notice()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
