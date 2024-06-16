import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class StatisticsApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.input_field = QLineEdit()
        self.run_button = QPushButton("Run")
        self.clear_button = QPushButton("Clear")
        self.output_field = QTextEdit()

        self.run_button.clicked.connect(self.run_code)
        self.clear_button.clicked.connect(self.clear_fields)

        layout = QVBoxLayout()
        layout.addWidget(self.input_field)
        layout.addWidget(self.run_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.output_field)

        self.setLayout(layout)

        self.setWindowTitle("Statistics")
        self.show()

    def run_code(self):
        user_input = self.input_field.text()
        try:
            # Parse the input as a list of numbers
            numbers = list(map(float, user_input.split(',')))
            
            # Calculate statistics
            percentile_75 = np.percentile(numbers, 75)
            percentile_25 = np.percentile(numbers, 25)
            q1 = np.percentile(numbers, 25)
            q3 = np.percentile(numbers, 75)
            iqr = q3 - q1
            correlation = np.corrcoef(numbers, numbers)[0, 1]
            regression_coefficient = np.polyfit(range(len(numbers)), numbers, 1)[0]
            
            self.output_field.append("Input Numbers:\n" + str(numbers) + "\n")
            self.output_field.append("75th Percentile: " + str(percentile_75) + "\n")
            self.output_field.append("25th Percentile: " + str(percentile_25) + "\n")
            self.output_field.append("Q1: " + str(q1) + "\n")
            self.output_field.append("Q3: " + str(q3) + "\n")
            self.output_field.append("Interquartile Range: " + str(iqr) + "\n")
            self.output_field.append("Correlation Coefficient: " + str(correlation) + "\n")
            self.output_field.append("Regression Coefficient: " + str(regression_coefficient) + "\n")
        except Exception as e:
            self.output_field.append(str(e))

    def clear_fields(self):
        self.input_field.clear()
        self.output_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = StatisticsApp()
    sys.exit(app.exec_())