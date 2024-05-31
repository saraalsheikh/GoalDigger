import sys
import os
import unittest
from PyQt5.QtWidgets import QApplication, QTextEdit, QPushButton, QAction, QFileDialog
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from unittest.mock import patch, mock_open
from journal_window import UI_journal_window  # Assuming the file name is journal_window.py

class TestUIJournalWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up the QApplication instance."""
        cls.app = QApplication(sys.argv)

    def setUp(self):
        """Set up the test case."""
        self.main_window = UI_journal_window()

    def test_new_file(self):
        """Test the newFile method."""
        self.main_window.txt_box.setText("Some text")
        QTest.mouseClick(self.main_window.action_new, Qt.LeftButton)
        self.assertEqual(self.main_window.txt_box.toPlainText(), "")
        self.assertEqual(self.main_window.windowTitle(), "Untitled")
        self.assertIsNone(self.main_window.current_path)

    @patch("builtins.open", new_callable=mock_open, read_data="Some text")
    @patch("PyQt5.QtWidgets.QFileDialog.getSaveFileName")
    def test_save_file_as(self, mock_get_save_file_name, mock_file):
        """Test the saveFileAs method."""
        mock_get_save_file_name.return_value = ('/fakepath/fakefile.txt', 'Text Documents (*.txt)')
        self.main_window.txt_box.setText("Some text")
        QTest.mouseClick(self.main_window.action_save_as, Qt.LeftButton)
        mock_file().write.assert_called_once_with("Some text")
        self.assertEqual(self.main_window.windowTitle(), "fakefile.txt")
        self.assertEqual(self.main_window.current_path, '/fakepath/fakefile.txt')

    @patch("builtins.open", new_callable=mock_open, read_data="Some text")
    @patch("PyQt5.QtWidgets.QFileDialog.getOpenFileName")
    def test_open_file(self, mock_get_open_file_name, mock_file):
        """Test the openFile method."""
        mock_get_open_file_name.return_value = ('/fakepath/fakefile.txt', 'Text Documents (*.txt)')
        QTest.mouseClick(self.main_window.action_open, Qt.LeftButton)
        self.assertEqual(self.main_window.txt_box.toPlainText(), "Some text")
        self.assertEqual(self.main_window.windowTitle(), "fakefile.txt")
        self.assertEqual(self.main_window.current_path, '/fakepath/fakefile.txt')

    def test_undo_redo(self):
        """Test the undo and redo methods."""
        self.main_window.txt_box.setText("Some text")
        self.main_window.txt_box.append("More text")
        QTest.mouseClick(self.main_window.action_undo, Qt.LeftButton)
        self.assertEqual(self.main_window.txt_box.toPlainText(), "Some text")
        QTest.mouseClick(self.main_window.action_redo, Qt.LeftButton)
        self.assertEqual(self.main_window.txt_box.toPlainText(), "Some text\nMore text")

    def test_cut_copy_paste(self):
        """Test the cut, copy, and paste methods."""
        self.main_window.txt_box.setText("Some text")
        self.main_window.txt_box.selectAll()
        QTest.mouseClick(self.main_window.action_cut, Qt.LeftButton)
        self.assertEqual(self.main_window.txt_box.toPlainText(), "")
        QTest.mouseClick(self.main_window.action_paste, Qt.LeftButton)
        self.assertEqual(self.main_window.txt_box.toPlainText(), "Some text")

    def test_set_dark_mode(self):
        """Test the setDarkMode method."""
        QTest.mouseClick(self.main_window.action_set_dark_mode, Qt.LeftButton)
        self.assertIn("background-color: rgb(33, 33, 33);", self.main_window.styleSheet())

    def test_set_light_mode(self):
        """Test the setLightMode method."""
        QTest.mouseClick(self.main_window.action_set_light_mode, Qt.LeftButton)
        self.assertEqual(self.main_window.styleSheet(), "")

    def test_increase_decrease_font_size(self):
        """Test the incFontSize and decFontSize methods."""
        initial_size = self.main_window.current_fontsize
        QTest.mouseClick(self.main_window.action_increase_font_size, Qt.LeftButton)
        self.assertEqual(self.main_window.current_fontsize, initial_size + 1)
        QTest.mouseClick(self.main_window.action_decrease_font_size, Qt.LeftButton)
        self.assertEqual(self.main_window.current_fontsize, initial_size)

    def test_btn_home_page_function(self):
        """Test the btn_home_page_function method."""
        with patch.object(self.main_window.signal_object, 'emit') as mock_emit:
            QTest.mouseClick(self.main_window.btn_home_page, Qt.LeftButton)
            mock_emit.assert_called_once()

    def tearDown(self):
        """Tear down the test case."""
        self.main_window.close()

if __name__ == "__main__":
    unittest.main()
