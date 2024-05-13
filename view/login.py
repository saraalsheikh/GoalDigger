import os
import sys
# This should point to the directory *above* your package if MVC_example is considered a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *


class UI_login_window(QMainWindow):
  def __init__(self):
    super(UI_login_window, self).__init__()
    uic.loadUi("view/uifiles/login_window.ui", self)
    self.btn_login = self.findChild(QPushButton, "btn_login")
    self.btn_login.clicked.connect(self.button_login_pushed)
    self.txt_username = self.findChild(QTextEdit, "txt_username")
    



    self.show()

  def button_login_pushed(self):
    username = self.txt_username.toPlainText()
    print(username)