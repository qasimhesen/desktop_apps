import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication , QWidget , QMainWindow , QPushButton , QProgressBar ,  QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QProgressButton example")
        self.resize(450 , 600)

        main_widget = QWidget(self)

        layout = QVBoxLayout()

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0 , 50)
        self.progress_bar.setValue(100)
        self.progress_bar.setTextVisible(True)

        self.start_button = QPushButton("click me please" , self)
        self.start_button.clicked.connect(self.start_task)

        layout.addWidget(self.progress_bar)
        layout.addWidget(self.start_button)
 
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.progress_value = 100




    def start_task(self):
        self.start_button.setDisabled(True)
        self.timer.start(1000)



    def update_progress(self):
        self.progress_value -= 12.5

        self.progress_bar.setValue(self.progress_value)
        if self.progress_value <= 0:
            self.timer.stop()
            self.start_button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


