import unittest
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from unittest.mock import patch, MagicMock
from view.uisignupwindow import UIsignupwindow  # Se till att importera rätt

class TestUISignupWindow(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Skapar en QApplication instans

    def setUp(self):
        self.window = UI_signup_window()
        self.window.show()  # Visar fönstret för testning

    def tearDown(self):
        self.window.close()  # Stänger fönstret efter varje test

    @patch('controller.controller.Controller.insert_new_user')
    def test_signup_function(self, mock_insert_new_user):
        # Mocka kontrollerens insert_new_user metod
        mock_insert_new_user.return_value = None

#Simulera textinmatning i textfälten
        self.window.txt_username.setText('testuser')
        self.window.txt_userid.setText('1234')
        self.window.txt_password.setText('password')

        # Klicka på signup knappen
        QTest.mouseClick(self.window.btn_signup, Qt.LeftButton)

#Verifiera att insert_new_user anropades med rätt parametrar
        mock_insert_new_user.assert_called_with('testuser', '1234', 'password')

        # Kontrollera att signalen sänds och fönstret stängs
        with self.assertRaises(RuntimeError):  # PyQt5 error när vi testar close()
            self.window.close()

    def test_login_function(self):
        # Kontrollera att signalen sänds och fönstret stängs när login knappen klickas
        with self.assertRaises(RuntimeError):  # PyQt5 error när vi testar close()
            self.window.btn_login.click()

if __name == '__main':
    unittest.main()