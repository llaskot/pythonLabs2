from controllers.rentController import search_rent
from viev_l2.TableView import TableSection
from viev_l2.table_abstract import TabAbstract


class RentsTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Rents', style)
        # left
        self.search_func = search_rent
        search_section = self._create_search_section("Rent search")
        self.left_layout.addWidget(search_section)
        # right
        self.table_section = TableSection(self.search_func(''))
        self.tablet_layout.addWidget(self.table_section)
