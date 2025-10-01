import tkinter as tk
from tkinter import ttk, messagebox
from sqlite3 import Error as sqlError
from controllers.clientController import search_client
from controllers.rentController import get_all_rents, change_statuses
from view.carsView import CarsView
from view.rentPopup import RentPopup
from view.tables import Tables


class RentView(CarsView):
    def __init__(self, master):
        super().__init__(master)

        self.search_label.config(text="Search Rent")
        self.label_id.config(text="Rent ID")
        self.add_button.config(text="Add Rent")
        self.danger.config(text="End rent")
        self.delete_button.forget()
        self.update_button.config(text="Car is back", command=self.end_rent)
        self.get_all_rows_func = get_all_rents

        self.search_func = search_client
        self.get_all_rows_func = get_all_rents

        self.car_data = get_all_rents()
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
        return RentPopup(self, client_id, on_close=self.update_table)

    def end_rent(self):
        try:
            res = change_statuses(self.car_id_var.get())
            if not res:
                messagebox.showerror("Rent status error", str(f"Rent #{self.car_id_var.get()} is already closed"))
            self.entry_id.delete(0, tk.END)
            self.update_table()
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except KeyError as e:
            messagebox.showerror("Empty fields error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))
