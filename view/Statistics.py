import os
import sys
from PyQt5.QtWidgets import QMainWindow
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout
from PyQt5 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from view.mood_tracker import MoodTrackerApp

class StatisticsWindow(QMainWindow):
    def __init__(self, mood_data):
        super(StatisticsWindow, self).__init__()
        uic.loadUi('view/uifiles/statistics_window.ui', self)
        
        self.list_clicked = self.findChild(QListWidget, "listWidget")

        self.list_clicked.connect()
    
    def get_mood(self):
        moods = [1, 4, 3, 5, 2, 1, 5]
        for mood in moods:
            self.list_widget.addItem(str(mood))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mood_data = {"happy": 10, "neutral": 5, "sad": 7, "very sad": 3, "very happy": 12}
    window = StatisticsWindow(mood_data)
    window.show()
    sys.exit(app.exec_())
