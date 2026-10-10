import sys
from PySide6.QtWidgets import QApplication

from pet import Pet


def main():
    app = QApplication(sys.argv)
    pet = Pet()

    pet.show()
    app.exec()

main()
