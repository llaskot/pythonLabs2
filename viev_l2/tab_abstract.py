from typing import Callable

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QLineEdit, QPushButton, QGroupBox


class TabAbstract(QWidget):
    def __init__(self, name: str, style: str):
        super().__init__()
        self.name = name
        self.style = style

        # main horizontal layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(2)

        # left panel
        self.left_side = QWidget(self)
        self.left_side.setFixedWidth(250)
        self.left_side.setStyleSheet("background-color: #a89036; border: 1px solid black;")
        self.layout.addWidget(self.left_side)
        self.left_layout = QVBoxLayout(self.left_side)
        self.left_layout.setContentsMargins(5, 5, 5, 5)
        self.left_layout.setSpacing(5)

        # right panel (tablet)
        self.tablet = QWidget(self)
        self.tablet.setStyleSheet("background-color: #7e36a8; border: 1px solid black;")
        self.layout.addWidget(self.tablet)
        self.tablet_layout = QVBoxLayout(self.tablet)

        # abstract
        self.search_func = None
        self.table_section = None
        # id from input
        self.id_val = None

    # will be defined and set in children
    def _create_search_section(self, label_text: str = "Label") -> QWidget:
        section = QWidget()
        layout = QVBoxLayout(section)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        section.setFixedHeight(100)

        label = QLabel(label_text, )
        label.setProperty("class", "search-label")
        label.setStyleSheet(self.style)
        label.setFixedHeight(50)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        input_field = QLineEdit()
        input_field.setProperty("class", "search-field")
        input_field.setStyleSheet(self.style)
        input_field.textChanged.connect(self.on_text_changed)

        layout.addWidget(label)
        layout.addWidget(input_field)

        return section

    def _create_add_btn(self, text: str = "Button", func: Callable[[], None] | None = None) -> QWidget:
        section = QWidget()
        layout = QVBoxLayout(section)
        layout.setContentsMargins(2, 2, 2, 2)
        layout.setSpacing(2)
        section.setFixedHeight(100)

        btn = QPushButton(text)
        btn.setProperty("class", "btn-green")
        btn.setStyleSheet(self.style)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        btn.clicked.connect(func)

        layout.addWidget(btn)
        return section

    def create_update_del_section(self, name: str, on_edit_func: Callable[[], None],
                                  on_delete_func: Callable[[], None] | None = None,
                                  edit_btn: str = 'Edit') -> QGroupBox:
        box = QGroupBox("Danger Zone")
        box.setProperty("class", "QGroupBox")
        box.setStyleSheet(self.style)
        box.setFixedHeight(200)
        layout = QVBoxLayout(box)
        self.id_val, inp_row = self.create_id_input(name)
        btns_row = self.create_del_upd_btns(on_edit_func, on_delete_func, edit_btn)

        layout.addWidget(inp_row)
        layout.addWidget(btns_row)
        return box

    def create_id_input(self, name: str) -> (QLineEdit, QGroupBox):
        box = QGroupBox()
        box.setFixedHeight(70)
        box_layout = QVBoxLayout(box)
        box_layout.setContentsMargins(1, 1, 1, 1)

        inner = QWidget()
        inner.setStyleSheet("background-color: #f5f5f5; border: none;")  #
        layout = QHBoxLayout(inner)

        input_line = QLineEdit()
        input_line.setStyleSheet("border: 1px solid black;")
        input_line.setValidator(QIntValidator(0, 9999))
        input_line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        text = QLabel(name)
        text.setStyleSheet("border: none; background: transparent;")

        layout.addWidget(text)
        layout.addWidget(input_line)
        box_layout.addWidget(inner)
        return input_line, box

    def create_del_upd_btns(self, on_edit_func: Callable[[], None],
                            on_delete_func: Callable[[], None] | None = None,
                            edit_btn: str = "Edit") -> QGroupBox:
        box = QGroupBox()
        box.setFixedHeight(70)
        box_layout = QVBoxLayout(box)
        box_layout.setContentsMargins(1, 1, 1, 1)

        inner = QWidget()
        inner.setStyleSheet("background-color: #f5f5f5; border: none;")  #
        layout = QHBoxLayout(inner)

        upd_btn = QPushButton(edit_btn)
        self.id_val.textChanged.connect(lambda text: upd_btn.setEnabled(bool(text)))
        upd_btn.setProperty("class", "btn-orange")
        upd_btn.setStyleSheet(self.style)
        upd_btn.setEnabled(False)
        upd_btn.clicked.connect(on_edit_func)

        layout.addWidget(upd_btn)

        if on_delete_func:
            del_btn = QPushButton("Delete")
            self.id_val.textChanged.connect(lambda text: del_btn.setEnabled(bool(text)))
            del_btn.setProperty("class", "btn-red")
            del_btn.setStyleSheet(self.style)
            del_btn.setEnabled(False)
            del_btn.clicked.connect(on_delete_func)
            layout.addWidget(del_btn)

        box_layout.addWidget(inner)
        return box

    def on_text_changed(self, text: str):
        filtered_data = self.search_func(text)
        self.table_section.proxy.sourceModel().data_list = filtered_data
        self.table_section.proxy.sourceModel().layoutChanged.emit()
