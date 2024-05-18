import os
import sys
from PyQt5.QtWidgets import QWidget
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from view.signup import UI_signup_window

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
        # self.error = self.find(QLabel, "error")

        # Code that hides the password
        self.txt_password.setEchoMode(QLineEdit.Password)

        self.btn_login.clicked.connect(self.loginfunction)
        self.btn_welcome.clicked.connect(self.welcomefunction)        


    def loginfunction(self):
        pass
    #      username = self.txt_username.text()
    #      password = self.txt_password.text()
    #     if len(username) == 0 or len(password) == 0:
    #         self.error.setText("Please fill in the empty boxes.")
    #     else:
    #      self.error.setText("")  # Clear any previous error messages
    #      # Proceed with login logic here?? OR MAYBE CONNECT TO THE DATABASE
    #      print(f"Username: {username}, Password: {password}")  # Example action

    def welcomefunction(self):
        self.signal_login.emit()
        self.close()
    
        

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UI_login_window()
#     window.show()
#     sys.exit(app.exec_())