import tkinter as tk

from controllers.clientController import get_all_clients, delete_client_by_id
from view.carsView import CarsView
from view.clientPopup import ClientPopup
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

    def update_table(self):
        self.search_entry.delete(0, tk.END)
        self.search_var.set('')
        self.table.destroy()
        self.car_data = get_all_clients()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.grid(row=0, column=0, sticky="nsew")

        self.vsb.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=self.vsb.set)
        self.hsb.configure(command=self.table.xview)
        self.table.configure(xscrollcommand=self.hsb.set)

    def delete_unit(self):
        try:
            return delete_client_by_id(self.entry_id.get())
        except Exception as e:
            raise e

