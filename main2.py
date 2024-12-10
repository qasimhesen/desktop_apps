import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QMainWindow, QWidget, QLineEdit, QPushButton
from datetime import datetime


def calculate_age():
    user_input = input_field.text()
    try:
        
        birth_date = datetime.strptime(user_input, "%d.%m.%Y")
        today = datetime.today()
        age_years = today.year - birth_date.year
        age_months = today.month - birth_date.month
        age_days = today.day - birth_date.day

        
        if age_days < 0:
            age_months -= 1
            previous_month = (today.month - 1) % 12 or 12
            days_in_prev_month = (datetime(today.year, previous_month + 1, 1) - datetime(today.year, previous_month, 1)).days
            age_days += days_in_prev_month

        if age_months < 0:
            age_years -= 1
            age_months += 12

        
        label.setText(f"{age_years} years {age_months} months {age_days} days old")
    except ValueError:
        label.setText("Invalid date format. Use DD.MM.YYYY")


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Age Calculator")
window.resize(400, 300)

label = QLabel("Enter your birth date (DD.MM.YYYY):")
input_field = QLineEdit()
button = QPushButton("Calculate Age")

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(input_field)
layout.addWidget(button)

central_widget = QWidget()
central_widget.setLayout(layout)
window.setCentralWidget(central_widget)

button.clicked.connect(calculate_age)

window.show()

app.exec()
