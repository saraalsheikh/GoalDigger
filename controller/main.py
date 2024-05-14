import os
import sys


# This should point to the directory *above* your package if MVC_example is considered a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication
from view.login import UI_login_window
<<<<<<< HEAD
from view.signup import UI_signup_window
=======
>>>>>>> main

def main():
    app = QApplication(sys.argv)
    main_window = UI_login_window()
    app.exec_()


if __name__ == "__main__":
    main()
