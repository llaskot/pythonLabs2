import tkinter as tk

from controllers.clientController import get_all_clients
from view.carsView import CarsView
from view.tables import Tables


class ClientView(CarsView):
    def __init__(self, master):
        super().__init__(master)

        self.search_label.config(text="Search Clients")
        self.label_id.config(text="Client ID")
        self.add_button.config(text="add client")

        self.car_data = get_all_clients()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.grid(row=0, column=0, sticky="nsew")


    def open_add_window(self, client_id=None):
        self.entry_id.delete(0, tk.END)
        return ClientPopup(self, client_id, on_close=self.update_table)