from PyQt5.QtWidgets import QHBoxLayout, QWidget, QVBoxLayout, QLabel, QLineEdit, QSizePolicy

from viev_l2.tab import TabAbstract


class CarTab(TabAbstract):
    def __init__(self, style):
        super().__init__('Cars')
        self.style = style
        search_section = self._create_search_section("Car Search")
        self.left_layout.addWidget(search_section)

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

        layout.addWidget(label)
        layout.addWidget(input_field)

        return section


