import sys
from PySide6.QtWidgets import (
    QCheckBox, QApplication, QCalendarWidget, QWidget, QVBoxLayout, QLabel,
    QLineEdit, QStackedWidget, QComboBox, QButtonGroup, QPushButton,
    QMessageBox, QMainWindow
)
from PySide6.QtCore import QTimer, Qt


class MainWindow(QMainWindow):
    def __init__(self):  # Konstruktor metodu düzgün yazıldı
        super().__init__()
        self.setWindowTitle("Calendar Example")
        self.resize(600, 400)

        # QStackedWidget yaradılır
        self.stacked_widget = QStackedWidget()

        # Calendar Widget yaradılır
        self.calendar_widget = QWidget()
        calendar_layout = QVBoxLayout()
        self.calendar = QCalendarWidget()
        self.button = QPushButton("Click Me")
        self.button.clicked.connect(self.on_click)  # Siqnal təyin edildi

        calendar_layout.addWidget(self.calendar)
        calendar_layout.addWidget(self.button, alignment=Qt.AlignCenter)
        self.calendar_widget.setLayout(calendar_layout)

        # Date Widget yaradılır
        self.date_widget = QWidget()
        self.date_label = QLabel()  # Bu label nəticəni göstərəcək
        date_layout = QVBoxLayout()
        date_layout.addWidget(self.date_label, alignment=Qt.AlignCenter)
        self.date_widget.setLayout(date_layout)

        # QStackedWidget'ə widget'lar əlavə edilir
        self.stacked_widget.addWidget(self.calendar_widget)
        self.stacked_widget.addWidget(self.date_widget)
        self.setCentralWidget(self.stacked_widget)

    def on_click(self):
        # Calendar'dan seçilmiş tarixi al və onu date_label-ə yaz
        selected_date = self.calendar.selectedDate().toString()
        self.date_label.setText(f"Selected Date: {selected_date}")
        self.stacked_widget.setCurrentWidget(self.date_widget)  # Görünüşü dəyişdir


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
