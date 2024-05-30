import os
import sys

from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget, QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from controller.controller import Controller 

class UI_kalender_window(QWidget):
    signal_object = pyqtSignal()

    def __init__(self, user_id):
        super(UI_kalender_window, self).__init__()
        ui_file_path = "view/uifiles/kalender.ui"
        uic.loadUi(ui_file_path, self)
        self.user_id = user_id
        self.btn_savechanges = self.findChild(QPushButton, "btn_savechanges")
        self.btn_addnew = self.findChild(QPushButton, "btn_addnew")
        self.dsip_kalender = self.findChild(QCalendarWidget, "dsip_kalender")
        self.tasklist = self.findChild(QListWidget, "listWidget")
        self.textedit = self.findChild(QTextEdit, "textEdit")
        self.dsip_kalender.selectionChanged.connect(self.calendarDatechanged)
        self.updateTaskList()
        self.btn_savechanges.clicked.connect(self.savechanges)
        self.selected_date = None
        self.controller = Controller()

    def calendarDatechanged(self):
        self.selected_date = self.dsip_kalender.selectedDate()

    def savechanges(self):
        self.text = self.textedit.toPlainText()
        plan = [self.text, self.selected_date, self.user_id]
        self.controller.insert_plan(plan)
        self.updateTaskList()
        self.textedit.clear()

    def updateTaskList(self):
        self.tasklist.clear()
        plan_list = self.controller.fetch_plans(self.user_id)
        for plan in plan_list:
            self.tasklist.addItem(plan)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_kalender_window()
    window.show()
    app.exec_()