import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

from statistics import mode, median
    

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numbers Input")
        self.setGeometry(100, 100, 100, 150)

        self.label = QLabel("Enter marks:")
        self.mode_label = QLabel("")
        self.median_label = QLabel("")
        self.entry = QLineEdit()
        self.button = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)
        layout.addWidget(self.mode_label)
        layout.addWidget(self.median_label)

        self.setLayout(layout)
        self.button.clicked.connect(self.calculate_marks)

    def calculate_marks(self):
        student_marks = self.entry.text()
        list_of_marks = [float(mark.strip()) for mark in student_marks.replace(',', ' ').split()]
        mode_number = mode(list_of_marks)
        median_number = median(list_of_marks)
        self.mode_label.setText(f"Mode: {mode_number}")
        self.median_label.setText(f"Median: {median_number}")  
        self.entry.clear()
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
