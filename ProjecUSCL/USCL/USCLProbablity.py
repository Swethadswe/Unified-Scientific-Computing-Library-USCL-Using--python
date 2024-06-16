import sys
import numpy as np
from scipy.stats import uniform, norm, binom
from scipy.special import entr
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class ProbabilityOperationsApp(QWidget):
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

        self.setWindowTitle("Probability Operations")
        self.show()

    def run_code(self):
        user_input = self.input_field.text()
        try:
            # Parse the input as a list of numbers
            numbers = list(map(float, user_input.split(',')))
            
            # Calculate probability operations
            pdf_uniform = uniform.pdf(numbers, loc=0, scale=1)
            cdf_uniform = uniform.cdf(numbers, loc=0, scale=1)
            pdf_normal = norm.pdf(numbers, loc=0, scale=1)
            cdf_normal = norm.cdf(numbers, loc=0, scale=1)
            pdf_binomial = binom.pmf(numbers, n=10, p=0.5)
            cdf_binomial = binom.cdf(numbers, n=10, p=0.5)
            entropy = entr(pdf_uniform)
            bayes_theorem = (pdf_normal * cdf_uniform) / cdf_normal
            
            self.output_field.append("Input Numbers:\n" + str(numbers) + "\n")
            self.output_field.append("Uniform PDF: " + str(pdf_uniform) + "\n")
            self.output_field.append("Uniform CDF: " + str(cdf_uniform) + "\n")
            self.output_field.append("Normal PDF: " + str(pdf_normal) + "\n")
            self.output_field.append("Normal CDF: " + str(cdf_normal) + "\n")
            self.output_field.append("Binomial PDF: " + str(pdf_binomial) + "\n")
            self.output_field.append("Binomial CDF: " + str(cdf_binomial) + "\n")
            self.output_field.append("Information Entropy: " + str(entropy) + "\n")
            self.output_field.append("Bayes' Theorem: " + str(bayes_theorem) + "\n")
        except Exception as e:
            self.output_field.append(str(e))

    def clear_fields(self):
        self.input_field.clear()
        self.output_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ProbabilityOperationsApp()
    sys.exit(app.exec_())