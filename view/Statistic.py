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
    signal_object = pyqtSignal()

    def __init__(self,  parent=None, user_id=None):
        super(UI_Statistic_window, self).__init__(parent)
        uic.loadUi("view/uifiles/Statistic.ui", self)

        # Finding Widgets
        self.btn_show = self.findChild(QPushButton, "btn_show")
        self.list = self.findChild(QListWidget, "listWidget")
        self.user_id = user_id

        self.btn_show.clicked.connect(self.btn_show_function)

        self.controller = Controller()
        self.showstat()

    def showstat(self):
        
        moods = self.controller.fetch_mood(self.user_id)
        

        self.list.clear()

        for mood in moods:
            self.list.addItem(mood)

    def btn_show_function(self):
        self.signal_object.emit()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_Statistic_window()
    window.show()
    sys.exit(app.exec_())