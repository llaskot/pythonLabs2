from PyQt5.QtWidgets import QMessageBox

from controllers.clientController import search_client, get_client_by_id, delete_client_by_id
from viev_l2.popup.popup_client_add import PopupClientAdd
from viev_l2.popup.popup_client_update import PopupClientUpdate
from viev_l2.tableView import TableSection
from viev_l2.tab_abstract import TabAbstract


class ClientTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Clients', style)

        # left
        self.search_func = search_client
        search_section = self._create_search_section("Client Search")
        self.left_layout.addWidget(search_section)
        add_btn = self._create_add_btn("Add Client", self._open_create_popup)
        self.left_layout.addWidget(add_btn)
        danger = self.create_update_del_section("Client ID", self.on_edit, self.on_delete)
        self.left_layout.addWidget(danger)

        # right
        self.table_section = TableSection(search_client(''))
        self.tablet_layout.addWidget(self.table_section)

    def _open_create_popup(self):
        popup = PopupClientAdd(self)
        parent_center = self.mapToGlobal(self.rect().center())
        popup_rect = popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        popup.move(popup_rect.topLeft())
        popup.exec_()
        pass

    def on_edit(self):
        try:
            entity = get_client_by_id(self.id_val.text())
            if entity["qty"] == 0:
                QMessageBox.warning(self, "Warning", f"Client {self.id_val.text()} Not found")
            else:
                popup = PopupClientUpdate(self, entity["values"][0])
                parent_center = self.mapToGlobal(self.rect().center())
                popup_rect = popup.frameGeometry()
                popup_rect.moveCenter(parent_center)
                popup.move(popup_rect.topLeft())
                popup.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        pass

    def on_delete(self):
        try:
            QMessageBox.question(self, "Confirm deletion", f"Do you really want to delete Client # {self.id_val.text()}")
            res = delete_client_by_id(self.id_val.text())
            if res["affected_rows"] == 0:
                QMessageBox.warning(self, "Warning", f"Client {self.id_val.text()} Not found")
            else:
                QMessageBox.information(self, "Success", f"Client {self.id_val.text()} deleted")
                self.on_text_changed('')
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
        pass
