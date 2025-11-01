from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout


class TabAbstract(QWidget):
    def __init__(self, name):
        super().__init__()
        self.name = name
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