#import os
import sys
#from PyQt5 import QtWidgets, uic
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
#import mysql.connector
import os
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIcon, QPixmap
import sys


# from view.mood_tracker import MoodTrackerApp

class MoodTrackerApp(QMainWindow):
    def __init__(self, user_id):
        self.user_id = user_id
        super(MoodTrackerApp, self).__init__()
        uic.loadUi("view/uifiles/mood_tracker_window.ui", self)

        # finding widgets
        self.happy_clicked = self.findChild(QPushButton, "btn_happy")
        self.nuetral_clicked = self.findChild(QPushButton, "btn_nuetral")
        self.sad_clicked = self.findChild(QPushButton, "btn_sad")
        self.verysad_clicked = self.findChild(QPushButton, "btn_verysad")
        self.veryhappy_clicked = self.findChild(QPushButton, "btn_veryhappy")

        # connect buttons to functions
        self.happy_clicked.clicked.connect(lambda: self.save_mood("happy"))
        self.nuetral_clicked.clicked.connect(lambda: self.save_mood("neutral"))
        self.sad_clicked.clicked.connect(lambda: self.save_mood("sad"))
        self.verysad_clicked.clicked.connect(lambda: self.save_mood("very sad"))
        self.veryhappy_clicked.clicked.connect(lambda: self.save_mood("very happy"))

    def savemood(self):
        statistic = [self.user_id]


    def mood(self):
        if 


       

    # @pyqtSlot()
    # def save_mood(self, mood):
    #     query = "INSERT INTO moods (mood, timestamp) VALUES (%s, NOW())"
    #     self.cursor.execute(query, (mood,))
    #     self.conn.commit()
    #     print(f"Mood '{mood}' saved to database.")

    def closeEvent(self, event):
        self.cursor.close()
        self.conn.close()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodTrackerApp()
    window.show()
    sys.exit(app.exec_())


class EmojiButtonApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(EmojiButtonApp, self).__init__()
        uic.loadUi('view/uifiles/mood_tracker_window.ui', self)

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

        # Customize each QPushButton to only display the emoji image
        self.setupEmojiButton(self.btnHappy, os.path.join(desktop_path, 'smiling-face-with-smiling-eyes.png'))
        self.setupEmojiButton(self.btnSad, os.path.join(desktop_path, 'slightly-frowing-face.png'))
        self.setupEmojiButton(self.btnAngry, os.path.join(desktop_path, 'grinning-face.png'))
        self.setupEmojiButton(self.btnSurprised, os.path.join(desktop_path, 'neutral-face.png'))
        self.setupEmojiButton(self.btnNeutral, os.path.join(desktop_path, 'crying-face.png'))

        # # Customize each QPushButton to only display the emoji image
        # self.setupEmojiButton(self.btnHappy, 'path_to_happy_emoji.png')
        # self.setupEmojiButton(self.btnSad, 'path_to_sad_emoji.png')
        # self.setupEmojiButton(self.btnAngry, 'path_to_angry_emoji.png')
        # self.setupEmojiButton(self.btnSurprised, 'path_to_surprised_emoji.png')
        # self.setupEmojiButton(self.btnNeutral, 'path_to_neutral_emoji.png')

    def setupEmojiButton(self, button, image_path):
        button.setIcon(QIcon(QPixmap(image_path)))
        button.setIconSize(button.size())
        button.setStyleSheet("border: none; background: none;")

app = QtWidgets.QApplication(sys.argv)
window = EmojiButtonApp()
window.show()
sys.exit(app.exec_())

