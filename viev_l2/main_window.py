import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolBar, QSizePolicy, QWidget, QVBoxLayout, \
    QButtonGroup

from viev_l2.car import CarTab
from viev_l2.rents import RentsTab
from viev_l2.tab import TabAbstract


class MainWindow(QMainWindow):
    STYLE_PATH = os.path.join(os.path.dirname(__file__), "styles", "styles.qss")
    try:
        with open(STYLE_PATH) as f:
            BUTTON_STYLE = f.read()
    except FileNotFoundError:
        BUTTON_STYLE = ""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cars Rent Database GUI")
        self.resize(800, 400)

        # get main content
        self.contents = [RentsTab(), CarTab(self.BUTTON_STYLE), TabAbstract("Users")]

        # fill in main_page elements
        central_holder_layout, central_holder = self.create_central_holder()
        tool_bar = self.create_tool_bar([(cont.name, i) for i, cont in enumerate(self.contents)])
        for i, tab in enumerate(self.contents):
            central_holder_layout.addWidget(tab)
            if i != 0:  # hide tabs except 0
                tab.hide()

        # place main_page elements
        self.addToolBar(tool_bar)
        self.setCentralWidget(central_holder)

    def create_central_holder(self) -> (QVBoxLayout, QWidget):
        central = QWidget()
        central_layout = QVBoxLayout(central)
        central_layout.setContentsMargins(0, 0, 0, 0)
        central_layout.setSpacing(5)
        return central_layout, central

    def create_tool_bar(self, btns: list[tuple]) -> QToolBar:
        tabs_toolbar = QToolBar("Tabs")

        # buttons group for control
        btn_group = QButtonGroup(self)
        btn_group.setExclusive(True)
        btn_group.buttonClicked[int].connect(self.select_tab)

        for text, num in btns:
            btn = self.add_styled_button(text,"btn-blue")
            if num == 0:
                btn.setChecked(True)
            btn_group.addButton(btn, num)
            tabs_toolbar.addWidget(btn)
        return tabs_toolbar

    def add_styled_button(self, text: str,  class_name: str) -> QPushButton:
        btn = QPushButton(text)
        btn.setProperty("class", class_name)
        btn.setCheckable(True)
        btn.setStyleSheet(self.BUTTON_STYLE)
        btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        return btn

    def select_tab(self, tab_num: int = None):
        for tab in self.contents:
            tab.hide()
        self.contents[tab_num].show()


def run_lab2():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    app1 = QApplication(sys.argv)
    window1 = MainWindow()
    window1.show()
    sys.exit(app1.exec_())
