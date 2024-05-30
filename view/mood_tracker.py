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
<<<<<<< HEAD
    def __init__(self, user_id):
        self.user_id = user_id
        super(MoodTrackerApp, self).__init__()
=======
    signal_object = pyqtSignal()
    

    def __init__(self, parent=None, user_id=None):
        super(MoodTrackerApp, self).__init__(parent)
>>>>>>> main
        uic.loadUi("view/uifiles/mood_tracker_window.ui", self)
        self.user_id = user_id

        # finding widgets
        self.happy_clicked = self.findChild(QPushButton, "btn_happy")
        self.nuetral_clicked = self.findChild(QPushButton, "btn_nuetral")
        self.sad_clicked = self.findChild(QPushButton, "btn_sad")
        self.verysad_clicked = self.findChild(QPushButton, "btn_verysad")
        self.veryhappy_clicked = self.findChild(QPushButton, "btn_veryhappy")
        self.btn_home_page = self.findChild(QPushButton, "btn_home_page")
        self.btn_home_page.clicked.connect(self.btn_home_page_function)
        

        # connect buttons to functions
        self.happy_clicked.clicked.connect(lambda: self.save_mood(4))
        self.nuetral_clicked.clicked.connect(lambda: self.save_mood(3))
        self.sad_clicked.clicked.connect(lambda: self.save_mood(2))
        self.verysad_clicked.clicked.connect(lambda: self.save_mood(1))
        self.veryhappy_clicked.clicked.connect(lambda: self.save_mood(5))

<<<<<<< HEAD
    def savemood(self):
        statistic = [self.user_id]


    def mood(self):
        if 


       
=======
        self.user_mood = None
        self.controller = Controller()
>>>>>>> main

    def save_mood(self, mood):
        current_datetime = datetime.now()
        # current_datetime1 = current_datetime.toString("yyyy-MM-dd")
        self.user_mood = mood
        self.controller.insert_mood(self.user_mood, self.user_id, current_datetime)
        self.signal_object.emit()
        self.close()

    def btn_home_page_function(self):
        self.signal_object.emit()
        self.close()

<<<<<<< HEAD
    def closeEvent(self, event):
        self.cursor.close()
        self.conn.close()
        event.accept()
=======
>>>>>>> main


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodTrackerApp()
    window.show()
    sys.exit(app.exec_())
