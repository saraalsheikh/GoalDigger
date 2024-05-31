import os
import sys

# This should point to the directory *above* your package if MVC_example is considered a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import QApplication
from view.welcome import WelcomeScreen


def main():
    app = QApplication(sys.argv)
    main_window = WelcomeScreen()
    app.exec_()


if __name__ == "__main__":
    main()
