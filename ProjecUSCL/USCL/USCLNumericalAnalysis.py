import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class NumericalAnalysisApp(QWidget):
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

        self.setWindowTitle("Numerical Analysis")
        self.show()

    def run_code(self):
        user_input = self.input_field.text()
        try:
            # Parse the input as a list of numbers
            numbers = list(map(float, user_input.split(',')))
            
            # Calculate numerical analysis metrics
            mean = np.mean(numbers)
            median = np.median(numbers)
            mode = self.calculate_mode(numbers)
            variance = np.var(numbers)
            std_dev = np.std(numbers)
            
            self.output_field.append("Input Numbers:\n" + str(numbers) + "\n")
            self.output_field.append("Mean: " + str(mean) + "\n")
            self.output_field.append("Median: " + str(median) + "\n")
            self.output_field.append("Mode: " + str(mode) + "\n")
            self.output_field.append("Variance: " + str(variance) + "\n")
            self.output_field.append("Standard Deviation: " + str(std_dev) + "\n")
        except Exception as e:
            self.output_field.append(str(e))

    def calculate_mode(self, numbers):
        # Simple mode calculation, assumes there is only one mode
        counts = {}
        for num in numbers:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        max_count = max(counts.values())
        mode = [num for num, count in counts.items() if count == max_count][0]
        return mode

    def clear_fields(self):
        self.input_field.clear()
        self.output_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NumericalAnalysisApp()
    sys.exit(app.exec_())