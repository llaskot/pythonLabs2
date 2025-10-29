import sys
from PyQt5.QtWidgets import QApplication, QWidget


from PyQt5.QtWidgets import QMainWindow, QTabWidget
from views.tab_users import UsersTab
from views.tab_orders import OrdersTab



app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("My First PyQt5 App")
window.resize(1200, 900)
window.show()

sys.exit(app.exec_())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database GUI")
        self.resize(800, 600)

        tabs = QTabWidget()
        tabs.addTab(UsersTab(), "Users")
        tabs.addTab(OrdersTab(), "Orders")
        self.setCentralWidget(tabs)