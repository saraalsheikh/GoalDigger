import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
import sys
import os

#Mocking the UI_signup_window class to avoid dependency issues
class UIsignupwindow(QMainWindow):
    signalobject = pyqtSignal()
    def init(self, parent=None):
        super(UIsignupwindow, self).init(parent)
        self.signalobject.emit()

#Import the actual UI_login_window
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file), '..')))
from view.login import UI_login_window

class TestLoginWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.form = UI_login_window()

    def test_initial_ui_state(self):
        self.assertIsNotNone(self.form.btn_login)
        self.assertIsNotNone(self.form.btn_signup)
        self.assertIsNotNone(self.form.txt_username)
        self.assertIsNotNone(self.form.txt_password)

    def test_login_button_click(self):
        QTest.mouseClick(self.form.btn_login, Qt.LeftButton)
        # Here you would test what happens when login button is clicked
        # For example, if you had some label to show login status, you could check its text

    def test_signup_button_click(self):
        QTest.mouseClick(self.form.btn_signup, Qt.LeftButton)
        self.assertIsInstance(self.form.signupwindow, UI_signup_window)
        self.assertFalse(self.form.isVisible())
        self.assertTrue(self.form.signupwindow.isVisible())

    @classmethod
    def tearDownClass(cls):
        cls.app = None

if __name == "__main":
    unittest.main()