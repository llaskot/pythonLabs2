from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, QComboBox


class FilterCombo(QComboBox):
    def __init__(self, get_list_func, parent=None):
        super().__init__(parent)
        self.get_users_list = safe_call(get_list_func)
        self.setEditable(True)
        self.setInsertPolicy(QComboBox.NoInsert)
        self.setFocusPolicy(Qt.StrongFocus)
        self.lineEdit().textEdited.connect(self.filter_items)
        self._items = get_list_func("")
        self.addItems(self._items)
        self.lineEdit().clear()

    def filter_items(self, text):
        cursor_pos = self.lineEdit().cursorPosition()
        self._items = self.get_users_list(text)
        self.clear()
        self.addItems(self._items)
        self.lineEdit().setText(text)
        self.lineEdit().setCursorPosition(cursor_pos)

    def get_id(self):
        return self._items[self.currentText()] if self._items and self.currentText() else None


def safe_call(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            QMessageBox.critical(None, "Error", str(e))
            return []

    return wrapper
