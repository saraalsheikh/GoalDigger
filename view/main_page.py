import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

from view.journal import UI_journal_window
from view.kalender import UI_kalender_window
from view.mood_tracker import MoodTrackerApp


class HomePage(QMainWindow):
    signal_login = pyqtSignal()

    def __init__(self):
        super(HomePage, self).__init__()
        uic.loadUi("view/uifiles/main_page.ui", self)

        # finding widgets
        self.journal_clicked = self.findChild(QPushButton, "btn_journal")
        self.calender_clicked = self.findChild(QPushButton, "btn_calender")
        self.logout_clicked = self.findChild(QPushButton, "btn_moodtracker")


        # connect buttons to functions
        self.journal_clicked.clicked.connect(self.journalfunction)
        self.calender_clicked.clicked.connect(self.calenderfunction)
        self.logout_clicked.clicked.connect(self.moodtrackerfunction)
       

    def journalfunction(self):
        self.journal_window = UI_journal_window()
        self.journal_window.show()

    def calenderfunction(self):
        self.calender_window = UI_kalender_window()
        self.calender_window.show()

    def moodtrackerfunction(self):
        self.moodtracker_window = MoodTrackerApp()
        self.moodtracker_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = HomePage()
    main_window.show()
    sys.exit(app.exec_())

