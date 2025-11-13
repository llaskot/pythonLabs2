import sys

from PyQt5.QtWidgets import QApplication

from test.test_db import BbTests
from viev_l2.main_window import  MainWindow as l3

from view.main_window import MainWindow as l2
import test.test_db as l1


if __name__ == "__main__":
    print("select job:\n 1 — laba1\n 2 — laba2\n 3 — laba3\n 4 — Exit")

    choice = input("Input number (1-3): ")
    app = None
    if choice == "1":
        print("Start lab1...")
        app = l1
    elif choice == "2":
        app = l2()
    elif choice == "3":
        qapp = QApplication(sys.argv)
        app = l3()
    else:
        print("Exit.")

    if app:
        app.run()
