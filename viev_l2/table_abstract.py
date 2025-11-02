from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSizePolicy, QLineEdit

from viev_l2.TableView import TableModel, TableSection


class TabAbstract(QWidget):
    def __init__(self, name, style):
        super().__init__()
        self.name = name
        self.style = style

        # основной горизонтальный layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)

        # левая панель
        self.left_side = QWidget(self)
        self.left_side.setFixedWidth(250)
        self.left_side.setStyleSheet("background-color: #a89036; border: 1px solid black;")
        self.layout.addWidget(self.left_side)
        self.left_layout = QVBoxLayout(self.left_side)
        self.left_layout.setContentsMargins(5, 5, 5, 5)
        self.left_layout.setSpacing(5)

        # правая зона (tablet)
        self.tablet = QWidget(self)
        self.tablet.setStyleSheet("background-color: #7e36a8; border: 1px solid black;")
        self.layout.addWidget(self.tablet)
        self.tablet_layout = QVBoxLayout(self.tablet)

        # abstract
        self.search_func = None
        self.table_section = None

    def _create_search_section(self, label_text: str = "Label") -> QWidget:
        section = QWidget()
        layout = QVBoxLayout(section)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        section.setFixedHeight(100)

        label = QLabel(label_text, )
        label.setProperty("class", "search-label")
        label.setStyleSheet(self.style)
        label.setFixedHeight(50)  # фиксированная высота
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  # ширина растягивается на родителя

        input_field = QLineEdit()
        input_field.setProperty("class", "search-field")
        input_field.setStyleSheet(self.style)
        input_field.textChanged.connect(self._on_text_changed)

        layout.addWidget(label)
        layout.addWidget(input_field)

        return section

    def _on_text_changed(self, text: str):
        filtered_data = self.search_func(text)  # список строк по текущему вводу
        new_model = TableModel(filtered_data)
        self.table_section.table.setModel(new_model)
