import sys
import argparse
from PyQt5.QtWidgets import QApplication
from password_generator_app import PasswordGeneratorApp


__version__ = '2.0.0'

def main():
    parser = argparse.ArgumentParser(description='Password Generator App')
    parser.add_argument('--version', action='store_true', help='Show program version')
    args = parser.parse_args()

    if args.version:
        print(__version__)
    else:
        # print('Running Password Generator...')
        app = QApplication(sys.argv)
        window = PasswordGeneratorApp()
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()