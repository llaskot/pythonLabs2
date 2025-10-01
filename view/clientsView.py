import tkinter as tk
from tkinter import ttk
from controllers.clientController import get_all_clients, delete_client_by_id, search_client
from view.carsView import CarsView
from view.clientPopup import ClientPopup
from view.tables import Tables


class ClientView(CarsView):
    def __init__(self, master):
        super().__init__(master)

        self.search_label.config(text="Search Clients")
        self.label_id.config(text="Client ID")
        self.add_button.config(text="add client")
        self.search_func = search_client
        self.get_all_rows_func = get_all_clients

        self.car_data = get_all_clients()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.grid(row=0, column=0, sticky="nsew")

        # вертикальный скролл
        self.vsb = ttk.Scrollbar(self.info_frame, orient="vertical", command=self.table.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")

        # горизонтальный скролл
        self.hsb = ttk.Scrollbar(self.info_frame, orient="horizontal", command=self.table.xview)
        self.hsb.grid(row=1, column=0, sticky="ew")

        self.table.configure(xscrollcommand=self.hsb.set, yscrollcommand=self.vsb.set)


    def open_add_window(self, client_id=None):
        self.entry_id.delete(0, tk.END)
        return ClientPopup(self, client_id, on_close=self.update_table)

    def delete_unit(self):
        try:
            return delete_client_by_id(self.entry_id.get())
        except Exception as e:
            raise e
