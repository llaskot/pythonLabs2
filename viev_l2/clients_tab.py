from controllers.clientController import search_client
from viev_l2.TableView import TableSection
from viev_l2.table_abstract import TabAbstract


class ClientTab(TabAbstract):
    def __init__(self, style: str):
        super().__init__('Clients', style)
        self.search_func = search_client
        search_section = self._create_search_section("Car Search")
        self.left_layout.addWidget(search_section)
        self.table_section = TableSection(self.search_func(''))
        self.tablet_layout.addWidget(self.table_section)
