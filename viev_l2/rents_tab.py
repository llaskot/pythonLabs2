from PyQt5.QtWidgets import QMessageBox

from controllers.clientController import search_client, get_client_by_id, delete_client_by_id
from controllers.rentController import search_rent
from viev_l2.popup.popup_client_add import PopupClientAdd
from viev_l2.popup.popup_client_update import PopupClientUpdate
from viev_l2.popup.popup_rent import PopupRent
from viev_l2.tableView import TableSection
from viev_l2.tab_abstract import TabAbstract


class RentsTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Rents', style)

        # left
        self.search_func = search_rent
        search_section = self._create_search_section("Rent Search")
        self.left_layout.addWidget(search_section)
        add_btn = self._create_add_btn("Rent Car", self._open_create_popup)
        self.left_layout.addWidget(add_btn)
        danger = self.create_update_del_section("Rent ID", self.on_edit)
        self.left_layout.addWidget(danger)

        # right
        self.table_section = TableSection(search_rent(''))
        self.tablet_layout.addWidget(self.table_section)

    def _open_create_popup(self):
        popup = PopupRent(self)
        parent_center = self.mapToGlobal(self.rect().center())
        popup_rect = popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        popup.move(popup_rect.topLeft())
        popup.exec_()
        pass

    def on_edit(self):
        # try:
        #     entity = get_client_by_id(self.id_val.text())
        #     if entity["qty"] == 0:
        #         QMessageBox.warning(self, "Warning", f"Client {self.id_val.text()} Not found")
        #     else:
        #         popup = PopupClientUpdate(self, entity["values"][0])
        #         parent_center = self.mapToGlobal(self.rect().center())
        #         popup_rect = popup.frameGeometry()
        #         popup_rect.moveCenter(parent_center)
        #         popup.move(popup_rect.topLeft())
        #         popup.exec_()
        # except Exception as e:
        #     QMessageBox.critical(self, "Error", str(e))
        pass