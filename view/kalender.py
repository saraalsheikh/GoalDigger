import os
import sys

from PyQt5.QtWidgets import QWidget, QListWidgetItem, QListWidget, QApplication

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from controller.controller import Controller 

class UI_kalender_window(QMainWindow):
    signal_object = pyqtSignal()

    def __init__(self, parent=None, user_id=None):
        super(UI_kalender_window, self).__init__(parent)
        ui_file_path = "view/uifiles/kalender.ui"
        uic.loadUi(ui_file_path, self)
        self.controller = Controller()
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
        self.btn_home_page = self.findChild(QPushButton, "btn_home_page")
        self.btn_home_page.clicked.connect(self.btn_home_page_function)
        

    def calendarDatechanged(self):
        self.selected_date = self.dsip_kalender.selectedDate()

    def savechanges(self):
        self.text = self.textedit.toPlainText()
        selected_date_str = self.selected_date.toString("yyyy-MM-dd")
        plan = [self.text, selected_date_str, self.user_id]
        self.controller.insert_plan(plan)
        self.updateTaskList()
        self.textedit.clear()

    def updateTaskList(self):
        self.tasklist.clear()
        plan_list = self.controller.fetch_plans(self.user_id)
        for plan in plan_list:
            self.tasklist.addItem(plan)

    def btn_home_page_function(self):
        self.signal_object.emit()
        self.close()
        

