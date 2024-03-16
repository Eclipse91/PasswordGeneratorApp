import random
import string
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QSlider, QMessageBox
from PyQt5.QtCore import Qt

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()

        self.custom_string_label = QLabel("Custom String:")
        self.layout.addWidget(self.custom_string_label)
        self.custom_string_input = QLineEdit("")
        self.custom_string_input.textChanged.connect(self.update_password)
        self.layout.addWidget(self.custom_string_input)

        self.insert_position_label = QLabel("Insert Custom String After Every:")
        self.layout.addWidget(self.insert_position_label)
        self.insert_position_slider = QSlider(Qt.Horizontal)
        self.insert_position_slider.setMinimum(1)
        self.insert_position_slider.setMaximum(10)
        self.insert_position_slider.setValue(1)
        self.insert_position_slider.setTickInterval(1)
        self.insert_position_slider.setTickPosition(QSlider.TicksBelow)
        self.insert_position_slider.valueChanged.connect(self.update_password)
        self.layout.addWidget(self.insert_position_slider)

        self.lowercase_label = QLabel("Lowercase letters length:")
        self.layout.addWidget(self.lowercase_label)
        self.lowercase_slider = QSlider(Qt.Horizontal)
        self.lowercase_slider.setMinimum(0)
        self.lowercase_slider.setMaximum(20)
        self.lowercase_slider.setValue(5)
        self.lowercase_slider.setTickInterval(1)
        self.lowercase_slider.setTickPosition(QSlider.TicksBelow)
        self.lowercase_slider.valueChanged.connect(self.update_password)
        self.layout.addWidget(self.lowercase_slider)

        self.uppercase_label = QLabel("Uppercase letters length:")
        self.layout.addWidget(self.uppercase_label)
        self.uppercase_slider = QSlider(Qt.Horizontal)
        self.uppercase_slider.setMinimum(0)
        self.uppercase_slider.setMaximum(20)
        self.uppercase_slider.setValue(5)
        self.uppercase_slider.setTickInterval(1)
        self.uppercase_slider.setTickPosition(QSlider.TicksBelow)
        self.uppercase_slider.valueChanged.connect(self.update_password)
        self.layout.addWidget(self.uppercase_slider)

        self.numbers_label = QLabel("Numbers length:")
        self.layout.addWidget(self.numbers_label)
        self.numbers_slider = QSlider(Qt.Horizontal)
        self.numbers_slider.setMinimum(0)
        self.numbers_slider.setMaximum(20)
        self.numbers_slider.setValue(2)
        self.numbers_slider.setTickInterval(1)
        self.numbers_slider.setTickPosition(QSlider.TicksBelow)
        self.numbers_slider.valueChanged.connect(self.update_password)
        self.layout.addWidget(self.numbers_slider)

        self.symbols_label = QLabel("Symbols length:")
        self.layout.addWidget(self.symbols_label)
        self.symbols_slider = QSlider(Qt.Horizontal)
        self.symbols_slider.setMinimum(0)
        self.symbols_slider.setMaximum(20)
        self.symbols_slider.setValue(1)
        self.symbols_slider.setTickInterval(1)
        self.symbols_slider.setTickPosition(QSlider.TicksBelow)
        self.symbols_slider.valueChanged.connect(self.update_password)
        self.layout.addWidget(self.symbols_slider)

        self.generate_button = QPushButton("Generate Password")
        self.generate_button.clicked.connect(self.generate_password)
        self.layout.addWidget(self.generate_button)

        self.password_label = QLabel("")
        self.layout.addWidget(self.password_label)

        self.setLayout(self.layout)

        self.update_password()

    def update_password(self):
        custom_string = self.custom_string_input.text()

        lowercase_length = self.lowercase_slider.value()
        uppercase_length = self.uppercase_slider.value()
        numbers_length = self.numbers_slider.value()
        symbols_length = self.symbols_slider.value()
        insert_position = self.insert_position_slider.value() - 1

        chars = ''
        chars += ''.join(random.choice(string.ascii_lowercase) for _ in range(lowercase_length))
        chars += ''.join(random.choice(string.ascii_uppercase) for _ in range(uppercase_length))
        chars += ''.join(random.choice(string.digits) for _ in range(numbers_length))
        chars += ''.join(random.choice(string.punctuation) for _ in range(symbols_length))

        password = ''.join(random.sample(chars, len(chars)))
        password = password[:insert_position] + custom_string + password[insert_position:]

        self.password_label.setText(password)

    def generate_password(self):
        self.update_password()

        # custom_string = self.custom_string_input.text()

        # if custom_string:
        #     password = self.password_label.text()
        #     insert_position = self.insert_position_slider.value() - 1
        #     password = password[:insert_position] + custom_string + password[insert_position:]
        #     self.password_label.setText(password)
