import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Set window title and size
        self.setWindowTitle("USCL Tools")
        self.setGeometry(0, 0, 1366, 768)

        # Set dark mode background image
        background_image = QPixmap("dark_mode_background.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 1366, 768)

        # Create buttons
        button1 = QPushButton("Matrix Multiplication", self)
        button1.setGeometry(50, 50, 200, 50)
        button1.clicked.connect(self.open_matrix_multiplication)

        button2 = QPushButton("Numerical Analysis", self)
        button2.setGeometry(50, 150, 200, 50)
        button2.clicked.connect(self.open_numerical_analysis)

        button3 = QPushButton("Probability Operations", self)
        button3.setGeometry(50, 250, 200, 50)
        button3.clicked.connect(self.open_probability_operations)

        button4 = QPushButton("Statistics", self)
        button4.setGeometry(50, 350, 200, 50)
        button4.clicked.connect(self.open_statistics)

        button5 = QPushButton("Cheat Sheet", self)
        button5.setGeometry(50, 450, 200, 50)
        button5.clicked.connect(self.open_cheat_sheet)

        button6 = QPushButton("Image Recognition", self)
        button6.setGeometry(50, 550, 200, 50)
        button6.clicked.connect(self.open_image_recognition)

        # Show window
        self.show()

    def open_matrix_multiplication(self):
        subprocess.Popen(["python", "USCL/USCLmatrix.py"])

    def open_numerical_analysis(self):
        subprocess.Popen(["python", "USCL/USCLNumericalAnalysis.py"])

    def open_probability_operations(self):
        subprocess.Popen(["python", "USCL/USCLProbablity.py"])

    def open_statistics(self):
        subprocess.Popen(["python", "USCL/USCLStatics.py"])

    def open_cheat_sheet(self):
        subprocess.Popen(["notepad", "cheatsheet.txt"])

    def open_image_recognition(self):
        subprocess.Popen(["python", "USCL/imageRecognization.py"])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())