import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QVBoxLayout
from PyQt5 import uic
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class StatisticsWindow(QMainWindow):
    def __init__(self, mood_data):
        super(StatisticsWindow, self).__init__()
        uic.loadUi('view/uifiles/statistics_window.ui', self)

        # Example data: mood counts
        self.mood_data = mood_data
        self.plot_statistics()

    def plot_statistics(self):
        moods = list(self.mood_data.keys())
        counts = list(self.mood_data.values())

        # Create the figure and the bar chart
        fig, ax = plt.subplots()
        ax.bar(moods, counts, color=['green', 'gray', 'blue', 'red', 'orange'])
        ax.set_ylabel('Count')
        ax.set_title('Mood Statistics')

        # Create a FigureCanvas and add it to the chartWidget
        canvas = FigureCanvas(fig)
        layout = QVBoxLayout(self.chartWidget)
        layout.addWidget(canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MoodTrackerApp()
    window.show()
    sys.exit(app.exec_())
