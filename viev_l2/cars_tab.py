
from controllers.carController import search_car
from viev_l2.TableView import TableSection, TableModel
from viev_l2.table_abstract import TabAbstract


class CarTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Cars', style)
        self.search_func = search_car
        search_section = self._create_search_section("Car Search")
        self.left_layout.addWidget(search_section)
        self.table_section = TableSection(search_car(''))
        self.tablet_layout.addWidget(self.table_section)







