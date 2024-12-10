import sys
import json
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QCheckBox, QPushButton, QMessageBox, QStackedWidget
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sorgu-sual")
        self.resize(600, 400)

        # Stack widgeti yarat
        self.stack_widget = QStackedWidget()

        # Login widgetini yarat
        self.login_widget = QWidget()
        login_layout = QVBoxLayout()  # Səhv burada düzəldildi

        # Username-i input kimi götür
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter the username")

        # Password-u input kimi götür
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter the password")
        self.password_input.setEchoMode(QLineEdit.Password)

        # Login as admin checkbox-u yarat
        self.admin_checkbox = QCheckBox("Login as Admin")

        # Login buttonunu yarat
        self.button = QPushButton("Login")
        self.button.setEnabled(False)
        self.button.clicked.connect(self.on_click)

        # Button-u aktivləşdir
        self.username_input.textChanged.connect(self.check_login)
        self.password_input.textChanged.connect(self.check_login)

        # Widget-ları əlavə et
        login_layout.addWidget(QLabel("Login page"), alignment=Qt.AlignCenter)
        login_layout.addWidget(self.username_input)
        login_layout.addWidget(self.password_input)
        login_layout.addWidget(self.admin_checkbox)
        login_layout.addWidget(self.button, alignment=Qt.AlignCenter)

        self.login_widget.setLayout(login_layout)

        # Admin widgeti
        self.admin_widget = QWidget()
        admin_layout = QVBoxLayout()
        admin_layout.addWidget(QLabel("Welcome. You logged in as admin"), alignment=Qt.AlignCenter)
        self.admin_widget.setLayout(admin_layout)

        # User widgeti
        self.user_widget = QWidget()
        user_layout = QVBoxLayout()
        user_layout.addWidget(QLabel("Welcome. You logged in as user"), alignment=Qt.AlignCenter)
        self.user_widget.setLayout(user_layout)

        # QStack-a widget-ləri əlavə et
        self.stack_widget.addWidget(self.login_widget)
        self.stack_widget.addWidget(self.admin_widget)
        self.stack_widget.addWidget(self.user_widget)

        self.setCentralWidget(self.stack_widget)

    def check_login(self):
        if len(self.username_input.text()) >= 5 and len(self.password_input.text()) >= 5:
            self.button.setEnabled(True)
        else:
            self.button.setEnabled(False)

    def on_click(self):
        username = self.username_input.text()
        password = self.password_input.text()
        is_admin = self.admin_checkbox.isChecked()

        try:
            with open("users.json", "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            self.show_message("Error", "User database not found.")
            return

        for user in users:
            if user['username'] == username and user['password'] == password:
                if is_admin and user['role'] == "admin":
                    self.show_message("Success", "Logged in as admin.")
                    self.stack_widget.setCurrentWidget(self.admin_widget)
                elif not is_admin and user['role'] == "user":
                    self.show_message("Success", "Logged in as user.")
                    self.stack_widget.setCurrentWidget(self.user_widget)
                else:
                    self.show_message("Error", "Invalid role selected.")
                return

        self.show_message("Error", "Invalid username or password.")

    def show_message(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec()

def main():
    
    users_data = [
        {"username": "admin", "password": "admin123", "role": "admin"},
        {"username": "user1", "password": "user123", "role": "user"}
    ]

    with open("users.json", "w") as f:
        json.dump(users_data, f, indent=4)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
