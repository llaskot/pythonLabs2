from PyQt5.QtWidgets import QMessageBox

from controllers.carController import search_car, get_car_by_id, delete_car_by_id
from viev_l2.TableView import TableSection
from viev_l2.popup.popup_car import PopupCar
from viev_l2.popup.popup_car_update import PopupCarUpdate
from viev_l2.tab_abstract import TabAbstract


class CarTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Cars', style)

        # left
        self.search_func = search_car
        search_section = self._create_search_section("Car Search")
        self.left_layout.addWidget(search_section)
        add_btn = self._create_add_btn("Add Car", self._open_create_popup)
        self.left_layout.addWidget(add_btn)
        danger = self.create_update_del_section("Car ID", self.on_edit, self.on_delete)
        self.left_layout.addWidget(danger)


        # right
        self.table_section = TableSection(search_car(''))
        self.tablet_layout.addWidget(self.table_section)


    def _open_create_popup(self):
        popup = PopupCar(self)
        # получаем глобальный центр родителя
        parent_center = self.mapToGlobal(self.rect().center())
        popup_rect = popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        popup.move(popup_rect.topLeft())
        popup.exec_()

    def on_edit(self):
        try:
            entity = get_car_by_id(self.id_val.text())
            if entity["qty"] == 0:
                QMessageBox.warning(self, "Warning", f"Car {self.id_val.text()} Not found")
            else:
                popup = PopupCarUpdate(self, entity["values"][0])
                parent_center = self.mapToGlobal(self.rect().center())
                popup_rect = popup.frameGeometry()
                popup_rect.moveCenter(parent_center)
                popup.move(popup_rect.topLeft())
                popup.exec_()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def on_delete(self):
        try:
            QMessageBox.question(self, "Confirm deletion", f"Do you really want to delete car # {self.id_val.text()}")
            res = delete_car_by_id(self.id_val.text())
            print(res)
            if res["affected_rows"] == 0:
                QMessageBox.warning(self, "Warning", f"Car {self.id_val.text()} Not found")
            else:
                QMessageBox.information(self, "Success", f"Car {self.id_val.text()} deleted")
                self.on_text_changed('')
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

