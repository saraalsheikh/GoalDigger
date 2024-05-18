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
        self.signup_window = UI_signup_window(self)
        self.signup_window.signal_object.connect(self.show)
        self.close()
        self.signup_window.show()
        

# if __name__ == "__main__":
#     app = QtWidgets.QApplication([])
#     welcome = WelcomeScreen()
#     welcome.show()
#     app.exec_()
