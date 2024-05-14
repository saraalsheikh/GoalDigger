import os
import sys

from PyQt5.QtWidgets import QWidget
# This should point to the directory *above* your package if MVC_example is considered a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from view.signup import UI_signup_window

class UI_login_window(QMainWindow):
    def __init__(self):
        super(UI_login_window, self).__init__()
        ui_file_path = "view/uifiles/login_window.ui"
        uic.loadUi("view/uifiles/login_window.ui", self)

        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_signup = self.findChild(QPushButton, "btn_signup")
        self.txt_username = self.findChild(QLineEdit, "txt_username")
        self.txt_password = self.findChild(QLineEdit, "txt_password")

        self.btn_login.clicked.connect(self.loginfunction)
        self.btn_signup.clicked.connect(self.signupfunction)
        self.show()

    def loginfunction(self):
        pass

    def signupfunction(self):
        self.signupwindow = UI_signup_window(self)
        self.signupwindow.signal_object.connect(self.show)
        
        self.close()
        self.signupwindow.show()

