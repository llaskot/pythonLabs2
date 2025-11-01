from PyQt5.QtWidgets import QHBoxLayout, QWidget


class CarTab(QWidget):
    def __init__(self):
        self.name = 'Cars'
        super().__init__()

        # основной горизонтальный layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # левая панель
        self.left_side = QWidget(self)
        self.left_side.setFixedWidth(100)
        self.left_side.setStyleSheet("background-color: #a89036; border: 1px solid black;")
        layout.addWidget(self.left_side)

        # правая зона (tablet)
        self.tablet = QWidget(self)
        self.tablet.setStyleSheet("background-color: #7e36a8; border: 1px solid black;")
        layout.addWidget(self.tablet)