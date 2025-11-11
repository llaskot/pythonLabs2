from PyQt5.QtWidgets import QMessageBox
from sqlite3 import Error as sqlError
from controllers.clientController import search_client, get_client_by_id, delete_client_by_id
from controllers.rentController import search_rent, change_statuses
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
        danger = self.create_update_del_section("Rent ID", self.on_edit, None, "Get the car back")
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

        entity = change_statuses(self.id_val.text())
        print(entity)

        try:
            entity = change_statuses(self.id_val.text())
            print(entity)

            if not entity:
                QMessageBox.warning(self, "Rent status error", str(f"Rent #{self.car_id_var.get()} is already closed"))
            self.update_table()
        except sqlError as e:
            QMessageBox.critical(self, "Database error", str(e))
        except KeyError as e:
            QMessageBox.critical(self, "Empty fields error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Something went wrong", str(e))

        pass