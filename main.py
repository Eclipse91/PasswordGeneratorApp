import sys
from PyQt5.QtWidgets import QApplication
from password_generator_app import PasswordGeneratorApp


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
