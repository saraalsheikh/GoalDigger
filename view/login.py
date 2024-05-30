import os
import sys
from PyQt5.QtWidgets import QWidget
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from view.signup import UI_signup_window
from controller.controller import Controller
from view.main_page import HomePage


class UI_login_window(QMainWindow):
    signal_login = pyqtSignal()

    def __init__(self):
        super(UI_login_window, self).__init__()
        uic.loadUi("view/uifiles/login_window.ui", self)

        # Finding Widgets
        self.btn_login = self.findChild(QPushButton, "btn_login")
        self.btn_welcome = self.findChild(QPushButton, "btn_welcome")
        self.txt_username = self.findChild(QLineEdit, "txt_username")
        self.txt_password = self.findChild(QLineEdit, "txt_password")
        self.error = self.find(QLabel, "error")

        # Code that hides the password
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_login.clicked.connect(self.loginfunction)
        self.btn_welcome.clicked.connect(self.welcomefunction) 
        self.error.setText("")       


    def loginfunction(self):
        username = self.txt_username.text()
        password = self.txt_password.text()
        self.controller = Controller()

        if len(username) == 0 or len(password) == 0:
            self.error.setText("Please fill in the empty boxes.")
        authenticate_user=self.controller.authenticate_user(username, password)
        if authenticate_user:
            userid = self.controller.fetch_user_id(username)
            self.home_page = HomePage(userid)
            self.home_page.signal_object.connect(self.show)
            self.close()
            self.home_page.show()
        else:
            pass


    def welcomefunction(self):
        self.signal_login.emit()
        self.close()
    
        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UI_login_window()
#     window.show()
#     sys.exit(app.exec_())