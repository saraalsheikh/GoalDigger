import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *


class UI_journal_window(QMainWindow):    
    signal_object = pyqtSignal()
    def __init__(self, parent=None, user_id=None):
        self.user_id=user_id
        super(UI_journal_window, self).__init__()
        ui_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'uifiles/journal_window.ui'))
        uic.loadUi(ui_file_path, self)

        self.current_path = None  # if current path is none, then there will be no file currently open
        self.current_fontsize = 8
        self.setWindowTitle("Untitled")  # When running the code, the title will now be set to Untitled rather than main

        # Finding the necessary widgets in the ui file
        self.txt_box = self.findChild(QTextEdit, "txt_box")  # Assuming the QTextEdit is named txt_box in the UI

        # Initializing actions
        self.action_new = self.findChild(QAction, "action_new")
        self.action_save = self.findChild(QAction, "action_save")
        self.action_save_as = self.findChild(QAction, "action_save_as")
        self.action_open = self.findChild(QAction, "action_open")
        self.action_undo = self.findChild(QAction, "action_undo")
        self.action_redo = self.findChild(QAction, "action_redo")
        self.action_cut = self.findChild(QAction, "action_cut")
        self.action_copy = self.findChild(QAction, "action_copy")
        self.action_paste = self.findChild(QAction, "action_paste")
        self.action_set_dark_mode = self.findChild(QAction, "action_set_dark_mode")
        self.action_set_light_mode = self.findChild(QAction, "action_set_light_mode")
        self.action_increase_font_size = self.findChild(QAction, "action_increase_font_size")
        self.action_decrease_font_size = self.findChild(QAction, "action_decrease_font_size")

        # Connecting actions to methods
        self.action_new.triggered.connect(self.newFile)
        self.action_save.triggered.connect(self.saveFile)
        self.action_save_as.triggered.connect(self.saveFileAs)
        self.action_open.triggered.connect(self.openFile)
        self.action_undo.triggered.connect(self.undo)
        self.action_redo.triggered.connect(self.redo)
        self.action_cut.triggered.connect(self.cut)
        self.action_copy.triggered.connect(self.copy)
        self.action_paste.triggered.connect(self.paste)
        self.action_set_dark_mode.triggered.connect(self.setDarkMode)
        self.action_set_light_mode.triggered.connect(self.setLightMode)
        self.action_increase_font_size.triggered.connect(self.incFontSize)
        self.action_decrease_font_size.triggered.connect(self.decFontSize)

    def newFile(self):
        self.txt_box.clear()
        self.setWindowTitle("Untitled")
        self.current_path = None  # This variable is important bc it will enable me to monitor whether we have a current file that is open
        print("New file clicked")

    def saveFile(self):
        if self.current_path is not None:
            # Save the changes without opening dialog
            filetext = self.txt_box.toPlainText()
            with open(self.current_path, 'w') as f:
                f.write(filetext)
        else:
            self.saveFileAs()
        print("Save file clicked")

    def saveFileAs(self):
        pathname, _ = QFileDialog.getSaveFileName(self, 'Save file', 'D:\\codefirst.io\\PyQt5 Text Editor', 'Text Documents (*.txt)')
        if pathname:  # Check if a valid path was selected
            filetext = self.txt_box.toPlainText()
            with open(pathname, 'w') as f:
                f.write(filetext)
            self.current_path = pathname
            self.setWindowTitle(os.path.basename(pathname))
        print("Save file as clicked")

    def openFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, "Open file", "D:\\codefirst.io\\PyQt5 Text Editor", "Text Documents (*.txt)")
        if fname:  # Check if a valid file was selected
            with open(fname, 'r') as f:
                filetext = f.read()
                self.txt_box.setText(filetext)
            self.current_path = fname
            self.setWindowTitle(os.path.basename(fname))
        print("Open clicked")

    def undo(self):
        self.txt_box.undo()
        print("Undo clicked")

    def redo(self):
        self.txt_box.redo()
        print("Redo clicked")

    def cut(self):
        self.txt_box.cut()
        print("Cut clicked")

    def copy(self):
        self.txt_box.copy()
        print("Copy clicked")

    def paste(self):
        self.txt_box.paste()
        print("Paste clicked")

    def setDarkMode(self):
        self.setStyleSheet(''' 
        QWidget{
            background-color: rgb(33, 33, 33);
            color: #FFFFFF
        }
        QTextEdit{
            background-color: rgb(46, 46, 46);
        }
        QMenuBar::item:selected{
            color: #000000
        } 
        ''')
        print("Set dark mode clicked")

    def setLightMode(self):
        self.setStyleSheet("")  # Empty string gives the default stylesheet
        print("Set light mode clicked")

    def incFontSize(self):
        self.current_fontsize += 1
        self.txt_box.setFontPointSize(self.current_fontsize)
        print("Increase font size clicked")
    
    def decFontSize(self):
        self.current_fontsize -= 1
        self.txt_box.setFontPointSize(self.current_fontsize)
        print("Decrease font size clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UI_journal_window()
    main_window.show()
    sys.exit(app.exec_())


