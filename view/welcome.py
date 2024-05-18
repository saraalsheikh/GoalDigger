# welcome.py
from PyQt5 import QtWidgets, uic
from view.login import UI_login_window
from view.signup import UI_signup_window

class WelcomeScreen(QtWidgets.QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        uic.loadUi("view/uifiles/welcomescreen.ui", self)
        
        self.btn_login_welcome = self.findChild(QtWidgets.QPushButton, 'btn_login_welcome')
        self.btn_signup_welcome = self.findChild(QtWidgets.QPushButton, 'btn_signup_welcome')

        self.btn_login_welcome.clicked.connect(self.go_to_login)
        self.btn_signup_welcome.clicked.connect(self.go_to_signup)
        self.show()

    def go_to_login(self):

        self.login_window = UI_login_window()
        self.login_window.signal_login.connect(self.show)

        self.close()
        self.login_window.show()
        

    def go_to_signup(self):
        self.signup_window = UI_signup_window()
        self.signup_window.signal_object.connect(self.show)
        self.close()
        self.signup_window.show()
        

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     welcome = WelcomeScreen()
#     welcome.show()
#     app.exec_()














# import os
# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import *
# from PyQt5 import uic
# from PyQt5.QtCore import *
# # from view.welcome_screen import UI_Welcome_screen

# class UI_Welcome_screen(QDialog):

#     signal_login = pyqtSignal()
#     signal_signup = pyqtSignal()

#     def __init__(self):
#         super(UI_Welcome_screen, self).__init__()
#         uic.loadUi("view/uifiles/welcomescreen.ui", self)

#         self.btn_login = self.findChild(QPushButton, "btn_login_welcome")
#         self.btn_signup = self.findChild(QPushButton, "btn_signup_welcome")

#         if not self.btn_login:
#             print("btn_login not found")
#         if not self.btn_signup:
#             print("btn_signup not found")

#         self.btn_login.clicked.connect(self.open_login)

#     def open_login(self):
#         self.signal_login.emit()

#     def open_sigup(self):
#         self.signal_login.emit()


# # remove when done bc its suppose to be in main

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UI_Welcome_screen()
#     window.show()
#     sys.exit(app.exec_())
