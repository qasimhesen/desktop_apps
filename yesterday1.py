import sys
from PySide6.QtWidgets import QApplication , QSpinBox, QLabel , QVBoxLayout , QPushButton, QWidget, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SPinBox example")
        self.resize(600 , 400)

        main_widget = QWidget(self)

        layout = QVBoxLayout()

        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0 , 100)
        self.spin_box.setValue(5)
        self.spin_box.setPrefix("$")

        self.first_label = QLabel("Choose the value" , self)

        self.button = QPushButton("Click the button" , self)
        self.button.clicked.connect(self.on_button_click)

        self.second_label = QLabel(self)

        layout.addWidget(self.first_label)
        layout.addWidget(self.spin_box)
        layout.addWidget(self.button)
        layout.addWidget(self.second_label)

        main_widget.setLayout(layout)

        self.setCentralWidget(main_widget)
        



    def on_button_click(self):
        value = self.spin_box.value()
        if value == 0:
            self.second_label.setText("Your choosen value is 0")
        else:
            self.second_label.setText(f"Choosen value is {value}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


