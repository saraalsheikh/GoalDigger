import os
import sys

from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget, QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

tasks = ["Mood", "To-Do"]
saved_tasks = []


class UI_kalender_window(QWidget):
    def __init__(self):
        super(UI_kalender_window, self).__init__()
        ui_file_path = "view/uifiles/kalender.ui"
        uic.loadUi(ui_file_path, self)

        self.btn_savechanges = self.findChild(QPushButton, "btn_savechanges")
        self.btn_addnew = self.findChild(QPushButton, "btn_addnew")
        self.dsip_kalender = self.findChild(QCalendarWidget, "dsip_kalender")
        self.tasklist = self.findChild(QListWidget, "listWidget")
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.dsip_kalender.selectionChanged.connect(self.calendarDatechanged)
        self.updateTaskList()
        self.btn_savechanges.clicked.connect(self.savechanges)
        self.selected_date = None

    def calendarDatechanged(self):
        self.selected_date = self.dsip_kalender.selectedDate()

    def savechanges(self):
        self.text = self.textedit.toPlainText()
        tasks.append(self.text)
        self.updateTaskList()
        saved_tasks.append((self.selected_date, self.text))
        self.textedit.clear()

    def updateTaskList(self):
        self.tasklist.clear()
        for task in tasks:
            self.tasklist.addItem(task)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_kalender_window()
    window.show()
    app.exec_()