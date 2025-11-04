from controllers.carController import search_car
from viev_l2.TableView import TableSection, TableModel
from viev_l2.popup.popup_car import PopupCar
from viev_l2.table_abstract import TabAbstract


class CarTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Cars', style)

        # left
        self.search_func = search_car
        search_section = self._create_search_section("Car Search")
        self.left_layout.addWidget(search_section)
        add_btn = self._create_add_btn("Add Car", self._open_create_popup)
        self.left_layout.addWidget(add_btn)


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
