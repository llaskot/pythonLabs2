from PyQt5.QtWidgets import QWidget, QHBoxLayout


class RentsTab(QWidget):
    def __init__(self):
        self.name = 'Rent'
        super().__init__()
        # основной горизонтальный layout
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)

        # левая панель
        self.left_side = QWidget(self)
        self.left_side.setFixedWidth(100)
        self.left_side.setStyleSheet("background-color: lightblue; border: 1px solid black;")
        layout.addWidget(self.left_side)

        # правая зона (tablet)
        self.tablet = QWidget(self)
        self.tablet.setStyleSheet("background-color: lightgreen; border: 1px solid black;")
        layout.addWidget(self.tablet)

