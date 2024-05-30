import sys
import os
from PyQt5.QtWidgets import QWidget
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

from view.journal import UI_journal_window
from view.kalender import UI_kalender_window
from view.mood_tracker import MoodTrackerApp


class HomePage(QMainWindow):
    signal_object = pyqtSignal()

    def __init__(self, parent=None, user_id=None):
        super(HomePage, self).__init__()
        uic.loadUi("view/uifiles/main_page.ui", self)

        # finding widgets
        self.journal_clicked = self.findChild(QPushButton, "btn_journal")
        self.calender_clicked = self.findChild(QPushButton, "btn_calender")
        self.moodtracker_clicked = self.findChild(QPushButton, "btn_mode_tracker")
        self.logout_clicked = self.findChild(QPushButton, "btn_logout")


        # connect buttons to functions
        self.journal_clicked.clicked.connect(self.journalfunction)
        self.calender_clicked.clicked.connect(self.calenderfunction)
        self.moodtracker_clicked.clicked.connect(self.moodtrackerfunction)
        # self.logout_clicked.clicked.connect(self.logoutfunction)
        self.user_id=user_id
       

    def journalfunction(self):
        self.journal_window = UI_journal_window(self.user_id)
        self.journal_window.signal_object.connect(self.show)
        self.close()
        self.journal_window.show()


    def calenderfunction(self):
        self.calender_window = UI_kalender_window(self.user_id)
        self.calender_window.signal_object.connect(self.show)
        self.close()
        self.calender_window.show()

    def moodtrackerfunction(self):
        self.moodtracker_window = MoodTrackerApp(self.user_id)
        self.moodtracker_window.signal_object.connect(self.show)
        self.close()
        self.moodtracker_window.show()

    # def logoutfunction(self):
    #     self.login_window = UI_login_window()
    #     self.close()
    #     self.login_window.show()        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HomePage()
    main_window.show()
    sys.exit(app.exec_())

