import random
import string
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QSlider, QFrame, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Password Generator')
        self.setGeometry(100, 100, 600, 300)

        self.layout = QHBoxLayout()

        # Left side: Password generator controls
        self.setup_password_generator()

        # Separator
        self.layout.addWidget(QFrame(frameShape=QFrame.VLine, frameShadow=QFrame.Sunken))

        # Right side: Password evaluator
        self.setup_password_evaluator()

        self.setLayout(self.layout)

        self.update_password()

    def setup_password_generator(self):
        generator_layout = QVBoxLayout()

        # Set the size policy for the generator layout (left side)
        for i in range(generator_layout.count()):
            item = generator_layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                # widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.custom_string_label = QLabel('Custom String:')
        generator_layout.addWidget(self.custom_string_label)

        self.custom_string_input = QLineEdit('')
        self.custom_string_input.textChanged.connect(self.update_password)
        generator_layout.addWidget(self.custom_string_input)

        self.insert_position_label = QLabel('Insert custom text in:')
        generator_layout.addWidget(self.insert_position_label)

        # For insert position slider
        self.insert_position_slider = QSlider(Qt.Horizontal)
        self.insert_position_slider.setMinimum(1)
        self.insert_position_slider.setMaximum(20)
        self.insert_position_slider.setValue(0)
        self.insert_position_slider.setTickInterval(1)
        self.insert_position_slider.setTickPosition(QSlider.TicksBelow)
        self.insert_position_slider.valueChanged.connect(self.update_insert_position_label)
        # Add a label to show the current value of the insert position slider
        self.insert_position_value_label = QLabel(str(self.insert_position_slider.value()) + '° position')
        generator_layout.addWidget(self.insert_position_value_label)
        generator_layout.addWidget(self.insert_position_slider)

        # Create a horizontal line (divider)
        self.divider = QFrame()
        self.divider.setFrameShape(QFrame.HLine)  # Horizontal line
        self.divider.setFrameShadow(QFrame.Sunken)  # Sunken effect
        # Add it to layout
        generator_layout.addWidget(self.divider)

        # For lowercase slider
        self.lowercase_label = QLabel('Lowercase letters length:')
        generator_layout.addWidget(self.lowercase_label)

        self.lowercase_slider = QSlider(Qt.Horizontal)
        self.lowercase_slider.setMinimum(0)
        self.lowercase_slider.setMaximum(20)
        self.lowercase_slider.setValue(0)
        self.lowercase_slider.setTickInterval(1)
        self.lowercase_slider.setTickPosition(QSlider.TicksBelow)
        self.lowercase_slider.valueChanged.connect(self.update_lowercase_label)

        # Add a label to show the current value of the lowercase slider
        self.lowercase_value_label = QLabel(str(self.lowercase_slider.value()))
        generator_layout.addWidget(self.lowercase_value_label)
        generator_layout.addWidget(self.lowercase_slider)

        # For uppercase slider (similar pattern as lowercase slider)
        self.uppercase_label = QLabel('Uppercase letters length:')
        generator_layout.addWidget(self.uppercase_label)

        self.uppercase_slider = QSlider(Qt.Horizontal)
        self.uppercase_slider.setMinimum(0)
        self.uppercase_slider.setMaximum(20)
        self.uppercase_slider.setValue(0)
        self.uppercase_slider.setTickInterval(1)
        self.uppercase_slider.setTickPosition(QSlider.TicksBelow)
        self.uppercase_slider.valueChanged.connect(self.update_uppercase_label)
        self.uppercase_value_label = QLabel(str(self.uppercase_slider.value()))
        generator_layout.addWidget(self.uppercase_value_label)
        generator_layout.addWidget(self.uppercase_slider)

        # For numbers slider (similar pattern as lowercase slider)
        self.numbers_label = QLabel('Numbers length:')
        generator_layout.addWidget(self.numbers_label)

        self.numbers_slider = QSlider(Qt.Horizontal)
        self.numbers_slider.setMinimum(0)
        self.numbers_slider.setMaximum(20)
        self.numbers_slider.setValue(0)
        self.numbers_slider.setTickInterval(1)
        self.numbers_slider.setTickPosition(QSlider.TicksBelow)
        self.numbers_slider.valueChanged.connect(self.update_numbers_label)
        self.numbers_value_label = QLabel(str(self.numbers_slider.value()))
        generator_layout.addWidget(self.numbers_value_label)
        generator_layout.addWidget(self.numbers_slider)

        self.symbols_label = QLabel('Symbols length:')
        generator_layout.addWidget(self.symbols_label)

        # For symbols slider (similar pattern as lowercase slider)
        self.symbols_slider = QSlider(Qt.Horizontal)
        self.symbols_slider.setMinimum(0)
        self.symbols_slider.setMaximum(20)
        self.symbols_slider.setValue(0)
        self.symbols_slider.setTickInterval(1)
        self.symbols_slider.setTickPosition(QSlider.TicksBelow)
        self.symbols_slider.valueChanged.connect(self.update_symbols_label)
        self.symbols_value_label = QLabel(str(self.symbols_slider.value()))
        generator_layout.addWidget(self.symbols_value_label)
        generator_layout.addWidget(self.symbols_slider)

        # Create a horizontal line (divider)
        self.divider = QFrame()
        self.divider.setFrameShape(QFrame.HLine)  # Horizontal line
        self.divider.setFrameShadow(QFrame.Sunken)  # Sunken effect
        # Add it to layout
        generator_layout.addWidget(self.divider)

        # Add a button to generate another password
        self.generate_button = QPushButton('Generate Password')
        self.generate_button.clicked.connect(self.update_password)
        generator_layout.addWidget(self.generate_button)

        # Add a button to copy the password
        self.copy_button = QPushButton('Copy Password')
        self.copy_button.clicked.connect(self.copy_password_to_clipboard)
        generator_layout.addWidget(self.copy_button)

        # Show the password
        self.password_label = QLabel('')
        self.password_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        generator_layout.addWidget(self.password_label)

        self.layout.addLayout(generator_layout)
        
    def update_insert_position_label(self, value):
        self.insert_position_value_label.setText(str(value) + '° position'  )
        self.update_password()

    def update_lowercase_label(self, value):
        self.lowercase_value_label.setText(str(value))
        self.update_password()

    def update_uppercase_label(self, value):
        self.uppercase_value_label.setText(str(value))
        self.update_password()

    def update_numbers_label(self, value):
        self.numbers_value_label.setText(str(value))
        self.update_password()

    def update_symbols_label(self, value):
        self.symbols_value_label.setText(str(value))
        self.update_password()

    def setup_password_evaluator(self):
        evaluator_layout = QVBoxLayout()
        
        # Set the size policy for the evaluator layout (right side)
        for i in range(evaluator_layout.count()):
            item = evaluator_layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.setSizePolicy(500,500)
                # widget.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        # Label to display the length of the generated password
        self.password_length_label = QLabel('Password Length:\n0')
        self.password_length_label.setAlignment(Qt.AlignCenter)
        evaluator_layout.addWidget(self.password_length_label)

        self.strength_label = QLabel('Password Strength:\n')
        self.strength_label.setAlignment(Qt.AlignCenter)
        evaluator_layout.addWidget(self.strength_label)
        
        # Add a label to display entropy
        self.entropy_label = QLabel('Entropy:\n0')
        self.entropy_label.setAlignment(Qt.AlignCenter)
        evaluator_layout.addWidget(self.entropy_label)

        self.strength_indicator = QLabel()
        self.strength_indicator.setAlignment(Qt.AlignCenter)
        self.strength_indicator.setStyleSheet('QLabel { background-color: red; border: 1px solid black; }')
        evaluator_layout.addWidget(self.strength_indicator)

        self.layout.addLayout(evaluator_layout)

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
        print(self.password_label.text())
        if self.password_label.text() == '':
            if chars == '':
                pass
            else:
                self.password_label.setText(password)
        else:
            if chars == '':
                pass
            elif len(self.password_label.text().splitlines()) < 10:
                self.password_label.setText(self.password_label.text() + '\n' + password)
            else:
                self.password_label.setText('\n'.join(self.password_label.text().splitlines()[-9:]) + '\n' + password)

        # Display the length of the generated password
        self.password_length_label.setText(f'Password Length:\n{len(password)}')
        self.password_length_label.setAlignment(Qt.AlignCenter)
        strength = self.evaluate_strength(password)
        self.strength_label.setText(f'Password Strength:\n{self.update_strength(strength)}')
        self.strength_label.setAlignment(Qt.AlignCenter)
        # Calculate and display entropy
        entropy = self.calculate_entropy(password)
        self.entropy_label.setText(f'Entropy:\n{entropy:.2f} bits')
        self.entropy_label.setAlignment(Qt.AlignCenter)

        # Evaluate password strength
        self.update_strength_indicator(strength)

    def evaluate_strength(self, password):
        strength = (len(password) - 6) // 3 + 1 if len(password) > 5 else 0

        # Check for character types
        types_present = [any(c in string.ascii_lowercase for c in password),
                         any(c in string.ascii_uppercase for c in password),
                         any(c in string.digits for c in password),
                         any(c in string.punctuation for c in password)]

        # Increase strength based on character types present
        strength += sum(types_present)

        return strength

    def update_strength_indicator(self, strength):
        # Set color based on strength level
        if strength <= 1:
            color = 'red'
        elif strength <= 3:
            color = 'orange'
        elif strength <= 5:
            color = 'yellow'
        elif strength <= 7:
            color = 'lime'
        elif strength <= 9:
            color = 'green'
        # elif strength <= 12:
        #     color = 'cyan'
        elif strength <= 15:
            color = 'blue'
        else: #if strength <= 18:
            color = 'indigo'
        # else:
        #     color = 'violet'

        self.strength_indicator.setStyleSheet(f'QLabel {{ background-color: {color}; border: 1px solid black; }}')
        self.strength_indicator.setText(f'Strength Level: {strength}')

    def update_strength(self, strength):
        if strength <= 1:
            strength_level = 'Very Weak'
        elif strength <= 3:
            strength_level = 'Weak'
        elif strength <= 5:
            strength_level = 'Moderate'
        elif strength <= 7:
            strength_level = 'Fair'
        elif strength <= 9:
            strength_level = 'Good'
        elif strength <= 12:
            strength_level = 'Strong'
        elif strength <= 15:
            strength_level = 'Very Strong'
        elif strength <= 18:
            strength_level = 'Excellent'
        else:
            strength_level = 'Outstanding'
        
        return strength_level

    def copy_password_to_clipboard(self):
        password = self.password_label.text().splitlines()[-1]
        if password:
            clipboard = QApplication.clipboard()
            clipboard.setText(password)
            # QMessageBox.information(self, 'Password Copied', 'Password copied to clipboard.')
        else:
            QMessageBox.warning(self, 'No Password', 'No password generated yet.')

    def calculate_entropy(self, password):
        # Count the number of possible characters in the password
        num_characters = [0, 0, 0, 0]

        for c in password:
            if c.islower():
                num_characters[0] = 26
            elif c.isupper():
                num_characters[1] = 26
            elif c.isdigit():
                num_characters[2] = 10
            elif c in string.punctuation:
                num_characters[3] = 32
                
            if 0 not in num_characters:
                break
        
        characters = sum(num_characters)
        # Check if num_characters is zero
        if characters == 0:
            return 0  # Return zero entropy if there are no characters

        # Calculate entropy in bits
        entropy = math.log2(characters) * len(password)
        return entropy