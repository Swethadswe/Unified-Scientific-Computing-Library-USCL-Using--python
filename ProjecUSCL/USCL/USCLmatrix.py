import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit

class MatrixMultiplicationApp(QWidget):
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

        self.setWindowTitle("USCL Matrix")
        self.show()

    def run_code(self):
        user_input = self.input_field.text()
        try:
            # Parse the input as a matrix multiplication problem
            matrices = user_input.split('*')
            matrix_A = np.array(eval(matrices[0]))
            matrix_B = np.array(eval(matrices[1]))
            
            # Check if the matrices can be multiplied
            if matrix_A.shape[1] != matrix_B.shape[0]:
                raise ValueError("Matrices cannot be multiplied")
            
            result = np.dot(matrix_A, matrix_B)
            self.output_field.append("Input Matrix A:\n" + str(matrix_A) + "\n")
            self.output_field.append("Input Matrix B:\n" + str(matrix_B) + "\n")
            self.output_field.append("Output Matrix:\n" + str(result) + "\n")
        except Exception as e:
            self.output_field.append(str(e))

    def clear_fields(self):
        self.input_field.clear()
        self.output_field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MatrixMultiplicationApp()
    sys.exit(app.exec_())