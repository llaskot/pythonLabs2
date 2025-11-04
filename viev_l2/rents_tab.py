from controllers.rentController import search_rent
from viev_l2.tableView import TableSection
from viev_l2.popup.popup_abstract import  PopupAbstract
from viev_l2.tab_abstract import TabAbstract


class RentsTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Rents', style)
        # left
        self.search_func = search_rent
        search_section = self._create_search_section("Rent search")
        self.left_layout.addWidget(search_section)
        add_btn = self._create_add_btn("Add Rent", self._open_create_popup)
        self.left_layout.addWidget(add_btn)

        # right
        self.table_section = TableSection(self.search_func(''))
        self.tablet_layout.addWidget(self.table_section)

    def _open_create_popup(self):
        popup = PopupAbstract(self)
        # получаем глобальный центр родителя
        parent_center = self.mapToGlobal(self.rect().center())
        popup_rect = popup.frameGeometry()
        popup_rect.moveCenter(parent_center)
        popup.move(popup_rect.topLeft())
        popup.exec_()

