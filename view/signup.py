import os
import sys
# This should point to the directory *above* your package if MVC_example is considered a package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *


class UI_signup_window(QMainWindow):
  def __init__(self):
    super(UI_signup_window, self).__init__()
    uic.loadUi("uifiles/signup_window.ui", self)



    self.show()

