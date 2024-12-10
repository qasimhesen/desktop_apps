import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication , QWidget , QMainWindow , QLabel , QLayout , QVBoxLayout , QSpinBox , QProgressBar, QLineEdit , QCheckBox , QComboBox , QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Sorgu-sual" )
        self.resize(600 , 400)

        self.questions = [
            {"type": "open", "question": "Who is the best teacher at the academy?", "answer": "ilkin"},
            {"type": "multiple", "question": "Which is the best programming languages?", "options": ["Python", "PHP", "Java"], "answer": ["Python"]},
            {"type": "single", "question": "Which is the best football team?", "options": ["Real Madrid", "Barcelona", "Chelsea"], "answer": "Chelsea"},
            {"type": "multiple", "question": "Which is the best car model?", "options": ["Changan", "Mercedes", "BMW"], "answer": ["Changan"]},
            {"type": "single", "question": "What is the color of the sky?", "options": ["Blue", "Green", "Red"], "answer": "Blue"}
        ]


        self.timer_remaining = 60

    
    
        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout(widget)


        self.timer_label = QLabel(f"Qalan muddet {self.timer_remaining}s")
        self.progress_bar = QProgressBar(maximum = self.timer_remaining , value = self.timer_remaining)

        layout.addWidget(self.timer_label)
        layout.addWidget(self.progress_bar)

        self.answer_widgets = []

        self.answer_widgets = []
        for q in self.questions:
            layout.addWidget(QLabel(q['question']))
            if q['type'] == 'open':
                answer_widget = QLineEdit()
                layout.addWidget(answer_widget)
            elif q['type'] == 'multiple':
                answer_widget = [QCheckBox(opt) for opt in q['options']]
                for checkbox in answer_widget:
                    layout.addWidget(checkbox)
            elif q['type'] == 'single':
                answer_widget = QComboBox()
                answer_widget.addItems(q['options'])
                layout.addWidget(answer_widget)
            self.answer_widgets.append(answer_widget)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)
        layout.addWidget(self.submit_button)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)


    def update_timer(self):
        self.timer_remaining -= 1

        self.timer_label.setText(f"Qalan vaxt {self.timer_remaining}")

        self.progress_bar.setValue(self.timer_remaining)

        if self.timer_remaining == 0:
            self.timer.stop()
            self.submit_button.setEnabled(False)

    def submit(self):
        self.timer.stop()
        correct = 0

        for i , q in enumerate(self.questions):
            widget = self.answer_widgets[i]
            if q['type'] == "open":
                if widget.text().strip().lower() == q['answer']:
                    correct += 1

            elif q['type'] == "multiple":
                selected = [checkbox.text() for checkbox in widget if checkbox.isChecked()]
                if set(selected) == set(q['answer']):
                    correct += 1

            elif q['type'] == "single":
                if widget.currentText() == q['answer']:
                    correct += 1

        if correct >= 4:
            result_label = QLabel("You win")

        else:
            result_label = QLabel("You lose")

        self.centralWidget().layout().addWidget(result_label)
        self.submit_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())




        


