from PyQt5.QtGui import QFont, QColor
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableView, QApplication, QHeaderView, QAbstractItemView
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
            font.setPointSize(12)
            return font
        elif role == Qt.BackgroundRole:
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
            font.setBold(True)
            font.setPointSize(12)
            return font
        elif role == Qt.BackgroundRole and orientation == Qt.Horizontal:
            return QColor("#e0e0e0")
        return None


class TableSection(QWidget):
    def __init__(self, data: dict):
        super().__init__()
        layout = QVBoxLayout(self)
        self.table = QTableView()
        header = self.table.horizontalHeader()
        header.setMinimumSectionSize(120)
        header.setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        model = TableModel(data)

        # proxy for sorting

        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(model)
        self.table.setModel(self.proxy)
        self.proxy.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.table.setSortingEnabled(True)

        # block interaction
        self.table.setSelectionMode(QTableView.NoSelection)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.table.setEditTriggers(QTableView.NoEditTriggers)
        self.table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)


