from PyQt5.QtWidgets import QMessageBox

from controllers.clientController import create_client
from viev_l2.popup.popup_client_abstract import PopupClientAbstract


class PopupClientUpdate(PopupClientAbstract):
    def __init__(self, parent, client: list):
        super().__init__(parent)
        self.client_data = client
        self.setWindowTitle("Update the client in the Database")
        self.main_content = self._create_main_content()
        self.layout.insertWidget(0, self.main_content)
        self.save_btn.clicked.connect(self._on_save)

    def _on_save(self):
        try:
            create_client((self.client_data[0], self.name_input.text(), self.license_input.text()))
            self.parent().on_text_changed('')
            self.close()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
