from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QApplication
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel


class TableModel(QAbstractTableModel):
    def __init__(self, data: dict):
        super().__init__()
        self.data_list = data
        self.headers = self.data_list['columns']

    def rowCount(self, parent=None):
        return self.data_list['qty']

    def columnCount(self, parent=None):
        return len(self.headers)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self.data_list['values'][index.row()][index.column()]
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignCenter
        elif role == Qt.FontRole:
            font = QFont()
            font.setPointSize(12)  # размер текста в ячейках
            return font
        elif role == Qt.BackgroundRole:
            # светло-серый фон для всех ячеек
            return QColor("#f5f5f5")
        else:
            return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self.headers[section]
            else:
                return None
        elif role == Qt.FontRole and orientation == Qt.Horizontal:
            font = QFont()
            font.setBold(True)  # жирный шрифт для заголовков
            font.setPointSize(12)  # размер шрифта заголовка
            return font
        elif role == Qt.BackgroundRole and orientation == Qt.Horizontal:
            # светло-серый фон заголовка
            return QColor("#e0e0e0")
        return None


class TableSection(QWidget):
    def __init__(self, data):
        super().__init__()
        layout = QVBoxLayout(self)
        self.table = QTableView()
        layout.addWidget(self.table)

        model = TableModel(data)

        # proxy для сортировки и фильтрации
        proxy = QSortFilterProxyModel()
        proxy.setSourceModel(model)
        self.table.setModel(proxy)

        proxy.setSortCaseSensitivity(Qt.CaseInsensitive)  # сортировка без учёта регистра

        self.table.setSortingEnabled(True)
