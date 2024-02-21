from PyQt5 import QtWidgets
from be_tt_display import Ui_be_tt_display
from text_notice_board import Ui_MainWindow
import sys
import threading


class Display_operations(object):
    def __init__(self):
        self.MainWindow = None
        self.be_tt_display = None

    def open_timetable(self):
        app = QtWidgets.QApplication(sys.argv)
        self.be_tt_display = QtWidgets.QMainWindow()
        ui = Ui_be_tt_display()
        ui.setupUi(self.be_tt_display)
        self.be_tt_display.show()
        sys.exit(app.exec_())

    def open_notice_board(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(self.MainWindow)
        self.MainWindow.showFullScreen()
        sys.exit(app.exec_())


class gesture_operations(object):
    open_obj = Display_operations()

    def timetable_opening_actions(self):
        self.open_obj.open_timetable()

    def notice_board_opening_actions(self):
        self.open_obj.open_notice_board()

    def active_operation_as_per_gesture_name(self, gesture_name):
        if gesture_name == "fist":
            open_timetable_thread = threading.Thread(target=self.timetable_opening_actions)
            open_timetable_thread.start()
            return True

        elif gesture_name == "thumbs up":
            open_notice_board_thread = threading.Thread(target=self.notice_board_opening_actions)
            open_notice_board_thread.start()
            return True
