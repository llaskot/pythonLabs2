# import inquirer

from viev_l2.main_window import run_lab2
from view.main_window import MainWindow



if __name__ == "__main__":
    print("Выбери лабораторную:")
    print("1 — lab1")
    print("2 — lab2")
    print("3 — выход")

    choice = input("Введите номер: ")

    if choice == "1":
        print("Запуск lab1...")
    elif choice == "2":
        app = MainWindow()
        app.run()
    elif choice == "3":
        run_lab2()
    else:
        print("Выход.")
