#import os
import sys
#from PyQt5 import QtWidgets, uic
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from controller.controller import Controller
from datetime import datetime
#import mysql.connector
# from view.mood_tracker import MoodTrackerApp

class MoodTrackerApp(QMainWindow):
    signal_object = pyqtSignal()
    

    def __init__(self, parent=None, user_id=None):
        super(MoodTrackerApp, self).__init__()
        uic.loadUi("view/uifiles/mood_tracker_window.ui", self)
        self.user_id = user_id

        # finding widgets
        self.happy_clicked = self.findChild(QPushButton, "btn_happy")
        self.nuetral_clicked = self.findChild(QPushButton, "btn_nuetral")
        self.sad_clicked = self.findChild(QPushButton, "btn_sad")
        self.verysad_clicked = self.findChild(QPushButton, "btn_verysad")
        self.veryhappy_clicked = self.findChild(QPushButton, "btn_veryhappy")

        # connect buttons to functions
        self.happy_clicked.clicked.connect(lambda: self.save_mood(4))
        self.nuetral_clicked.clicked.connect(lambda: self.save_mood(3))
        self.sad_clicked.clicked.connect(lambda: self.save_mood(2))
        self.verysad_clicked.clicked.connect(lambda: self.save_mood(1))
        self.veryhappy_clicked.clicked.connect(lambda: self.save_mood(5))

        self.user_mood = None
        self.controller = Controller()

    def save_mood(self, mood):
        current_datetime = datetime.now()
        self.user_mood = mood
        self.controller.insert_mood(self.user_mood, self.user_id, current_datetime)
        self.signal_object.emit()
        self.close()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodTrackerApp()
    window.show()
    sys.exit(app.exec_())
