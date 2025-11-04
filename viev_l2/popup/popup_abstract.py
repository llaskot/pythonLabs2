from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QGroupBox, QLineEdit, QHBoxLayout, \
    QWidget


class PopupAbstract(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('')
        self.setModal(True)  # делаем окно модальным
        # self.setFixedSize(300, 150)
        self.layout = QVBoxLayout(self)

        # abstract
        self.layout.addWidget(self.create_buttons_section())

    def create_buttons_section(self) -> QWidget:
        close_btn = QPushButton("Cancel")
        close_btn.clicked.connect(self.close)
        self.save_btn = QPushButton("Save")
        horizont_group = QWidget()
        hor_layout = QHBoxLayout(horizont_group)
        hor_layout.addWidget(self.save_btn)
        hor_layout.addWidget(close_btn)
        return horizont_group

    def create_text_input(self, name: str, val: str = '') -> (QLineEdit, QGroupBox):
        box = QGroupBox(name)
        layout = QVBoxLayout(box)
        input_line = QLineEdit(val)
        layout.addWidget(input_line)
        return input_line, box

    def create_int_input(self, name: str, val: str = '') -> (QLineEdit, QGroupBox):
        box = QGroupBox(name)
        layout = QVBoxLayout(box)
        input_line = QLineEdit(str(val))
        validator = QIntValidator(0, 9999)
        input_line.setValidator(validator)
        layout.addWidget(input_line)
        return input_line, box

    def create_float_input(self, name: str, val: str = '') -> (QLineEdit, QGroupBox):
        box = QGroupBox(name)
        layout = QVBoxLayout(box)
        input_line = QLineEdit(str(val))
        validator = QDoubleValidator(0.0, 999999.99, 2)  # min=0, max=9999, 2 знака после запятой
        validator.setLocale(QLocale(QLocale.C))
        validator.setNotation(QDoubleValidator.StandardNotation)
        input_line.setValidator(validator)
        layout.addWidget(input_line)
        return input_line, box
