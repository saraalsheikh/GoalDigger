import os
import sys

from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget, QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

from PyQt5.QtGui import *
from controller.controller import Controller


class UI_Statistic_window(QMainWindow):
    signal_login = pyqtSignal()

    def __init__(self, user_id):
        super(UI_Statistic_window, self).__init__()
        uic.loadUi("view/uifiles/Statistic.ui", self)

        # Finding Widgets
        self.btn_show = self.findChild(QPushButton, "btn_show")
        self.list = self.findChild(QListWidget, "listWidget")

        self.btn_show.clicked.connect(self.showstat)
        self.list.clicked.connect(self.updateTaskList)

        self.controller = Controller()

    def showstat(self):
        
        moods = [moods]
        days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]

        for i in range(len(moods)):
            item = "{}: {}".format(days[i], moods[i])
            self.list.addItem(item)


        average_mood = sum(moods) / len(moods)
        self.list.addItem("This is your average mood: {:.2f}".format(average_mood))

    def updateTaskList(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_Statistic_window()
    window.show()
    sys.exit(app.exec_())