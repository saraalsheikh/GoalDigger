# signup.py
import os
import sys
# This should point to the directory *above* your package if MVC_example is considered a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
from controller.controller import Controller


class UI_signup_window(QMainWindow):
  signal_object = pyqtSignal()


  def __init__(self, parent=None):
    super(UI_signup_window, self).__init__(parent)
    # The line below connects Gui to the iufile
    # I had to create a absolut path instead or relative path bc of file error handling 
    ui_file_path = "C:/Users/Surface/Desktop/Agile Project/GoalDigger/view/uifiles/signup_window.ui"
    uic.loadUi("view/uifiles/signup_window.ui", self)  # "view/uifiles/signup_window.ui"
    self.controller = Controller()
   
   
    # Finding the necessary widgets in the UI file
    self.btn_signup = self.findChild(QPushButton, "btn_signup")
    self.txt_username = self.findChild(QLineEdit, "txt_user_name")
    self.txt_password = self.findChild(QLineEdit, "txt_password")
    self.txt_confirm_password = self.findChild(QLineEdit, "txt_confirm_password")
    self.txt_userid = self.findChild(QLineEdit, "txt_user_id")
    self.btn_welcome = self.findChild(QPushButton, "btn_welcome")
    self.btn_welcome.clicked.connect(self.welcomefunction)



    # Code that hides the password snf vonfirm password fields
    self.txt_password.setEchoMode(QLineEdit.Password)
    self.txt_confirm_password.setEchoMode(QLineEdit.Password)

    # Connect the signup button to the signup function
    self.btn_signup.clicked.connect(self.signupfunction)

    


  # to create the function we create it inside the class but outside the constructor
  def signupfunction(self):
    # Below we are retrieving the text entered in the username, email, and password fields
    username = self.txt_username.text()
    user_id = self.txt_userid.text()
    password = self.txt_password.text()
    self.controller.insert_new_user(user_id, username, password)
    self.signal_object.emit()
    self.close()
  
  def loginfunction(self):
    self.signal_object.emit()
    self.close()

    
    #exampel how to get something from the database: 
    #self.allusers=self.controller.retrieve_all_users()

    # Print the information entered by the user
    

  def add_button_clicked(self):
    pass

  def welcomefunction(self):
      self.signal_object.emit()
      self.close()

# remove when done
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = UI_signup_window()
#     window.show()
#     sys.exit(app.exec_())