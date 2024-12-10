import sys
from PySide6.QtWidgets import QWidget,QApplication,QVBoxLayout,QMainWindow,QPushButton,\
QCalendarWidget,QLabel,QLineEdit
from PySide6.QtCore import Qt,QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("calendar exmaples")
        self.resize(400,600)
        central_widget = QWidget(self)
        self.calendar = QCalendarWidget(self)
        self.calendar.selectionChanged.connect(self.on_click) 
        self.label = QLabel()
        self.button = QPushButton("select date",self)
        self.button.clicked.connect(self.on_click)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def on_click(self):
        selected_date = self.calendar.selectedDate().toString()
        self.date_window = DateWindow(selected_date=selected_date)
        self.close()
        self.date_window.show()


class DateWindow(QWidget):
    def __init__(self,selected_date):
        super().__init__()
        self.setWindowTitle("result")
        self.resize(400,600)
        self.label = QLabel(selected_date)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)








def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()

