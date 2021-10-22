import sys
from password_generator import PasswordGenerator
from PyQt6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    app.exec()
