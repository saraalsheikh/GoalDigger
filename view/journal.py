import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTextEdit, QLineEdit
from PyQt5 import uic

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class UI_journal_window(QMainWindow):
    def __init__(self):
        super(UI_journal_window, self).__init__()
        ui_file_path = "view/uifiles/journal.ui"
        uic.loadUi(ui_file_path, self)

        # Finding the necessary widgets in the ui file
        self.btn_save = self.findChild(QPushButton, "btn_save")
        self.btn_cancel = self.findChild(QPushButton, "btn_cancel")
        self.txt_box = self.findChild(QTextEdit, "txt_box")
        self.txt_title = self.findChild(QLineEdit, "txt_title")

        # Connect the buttons to their respective functions
        self.btn_save.clicked.connect(self.savefunction)
        self.btn_cancel.clicked.connect(self.cancelfunction)

    def savefunction(self):
        # Get the text from the title and text box
        title = self.txt_title.text()
        content = self.txt_box.toPlainText()

        # Check if title or content is empty
        if not title or not content:
            QMessageBox.warning(self, "Warning", "Title or Content cannot be empty.")
            return

        # Save the content to a file
        filename = f"{title}.txt"
        with open(filename, 'w') as file:
            file.write(content)

        QMessageBox.information(self, "Success", "Journal entry saved successfully!")
        self.txt_title.clear()
        self.txt_box.clear()

    def cancelfunction(self):
        # Clear the text boxes
        self.txt_title.clear()
        self.txt_box.clear()
        QMessageBox.information(self, "Cancelled", "Journal entry cancelled.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UI_journal_window()
    main_window.show()
    sys.exit(app.exec_())
