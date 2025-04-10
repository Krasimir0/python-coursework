import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numbers Input")
        self.setGeometry(100, 100, 300, 150)

        self.label = QLabel("Enter numbers:")
        self.entry = QLineEdit()
        self.button = QPushButton("Submit")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.entry)
        layout.addWidget(self.button)

        self.setLayout(layout)
        self.button.clicked.connect(self.numbers_submit)

    def numbers_submit(self):
        numbers = self.entry.text()
        print("You entered:", numbers)
        self.entry.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
