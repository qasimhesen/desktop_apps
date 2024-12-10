import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSpinBox, QPushButton, QLabel
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox nümunəsi")
        self.resize(600,400)
        main_widget = QWidget(self)
        layout = QVBoxLayout()
        self.spin_box = QSpinBox(self)
        self.spin_box.setRange(0, 100)  
        self.spin_box.setValue(10)
        self.spin_box.setSuffix("₼")
        self.first_label = QLabel("Qiyməti seçin: ", self)
        self.button = QPushButton("Düyməni bas", self)
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
        self.second_label.setText(f"Seçilmiş qiymət: {value}")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())