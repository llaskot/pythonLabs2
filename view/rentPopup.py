from sqlite3 import Error as sqlError
import tkinter as tk
from tkinter import messagebox, ttk

from tkcalendar import Calendar, DateEntry

from controllers.carController import create_car, get_car_by_id
from controllers.rentController import get_users_list, get_cars_list, get_car
from view.clientPopup import ClientPopup


class RentPopup(tk.Toplevel):
    def __init__(self, master, rent_id=None, on_close=None):
        self.client_search_var = tk.StringVar(value='')
        self.cars_search_var = tk.StringVar(value='')

        self.on_close = on_close
        super().__init__(master)
        self.clients = {}
        self.get_filtered_clients()
        self.cars = {}
        self.get_filtered_cars()
        self.rent_id = rent_id

        self.client_fraim = tk.LabelFrame(self, text="Client", padx=5, pady=5)
        self.title("Add new rent" if not rent_id else f"Update the rent # {rent_id}")
        self.geometry("500x350")
        self.client_fraim = tk.LabelFrame(self, text="Client licence", padx=5, pady=5)
        self.client_fraim.pack(padx=10, pady=10, fill="x")
        self.clients_box = ttk.Combobox(self.client_fraim,
                                        values=list(self.clients.keys()),
                                        textvariable=self.client_search_var,
                                        )
        self.clients_box.pack(padx=10, pady=10, fill="x", side="left", expand=True)
        self.client_search_var.trace_add("write", self.update_user_box)
        self.add_client = tk.Button(self.client_fraim,
                                    # height=2,
                                    text="add Client",
                                    # bg="red",
                                    state="disabled",
                                    bd=4,
                                    command=self.open_add_window)
        self.add_client.pack(padx=10, pady=10, fill="x", side="left", expand=True)

        self.car_fraim = tk.LabelFrame(self, text="Car licence plate", padx=5, pady=5)
        self.car_fraim.pack(padx=10, pady=10, fill="x")
        self.car_box = ttk.Combobox(self.car_fraim,
                                    values=list(self.cars.keys()),
                                    textvariable=self.cars_search_var,
                                    )
        self.car_box.pack(padx=10, pady=10, fill="x", side="left", expand=True)
        self.cars_search_var.trace_add("write", self.update_car_box)

        date_var = tk.StringVar()
        date_entry = DateEntry(self, textvariable=date_var)
        date_entry.pack()


        tk.Button(self, text="Cancel", command=self.on_cancel).pack(pady=10, padx=15, side="left")
        tk.Button(self, text="Save", command=self.on_save).pack(pady=10, padx=15, side="right")

    def get_filtered_clients(self, *args):
        try:
            self.clients = get_users_list(self.client_search_var.get())
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))

    def get_filtered_cars(self, *args):
        try:
            self.cars = get_cars_list(self.cars_search_var.get())
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))

    def update_user_box(self, *args):
        try:
            self.clients = get_users_list(self.client_search_var.get())
            self.clients_box['values'] = list(self.clients.keys())
            if len(self.clients_box["values"]) == 0:
                    # and ": " not in self.client_search_var.get()):
                self.add_client['state'] = "normal"
            else:
                self.add_client['state'] = "disabled"
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))

    def update_car_box(self, *args):
        try:
            self.cars = get_cars_list(self.cars_search_var.get())
            self.car_box['values'] = list(self.cars.keys())
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))

    def open_add_window(self):
        popup = ClientPopup(self, on_close=self.update_user_box)
        popup.license_entry.insert(0, self.client_search_var.get())

    def on_cancel(self):
        if self.on_close:
            self.on_close()
        self.destroy()

    def on_save(self):

        try:
            print(self.car_box.get())
            print(self.cars)
            car = get_car(self.cars[self.car_box.get()])
            print(car)
            messagebox.showinfo("Success", "Successfully saved")
            # if self.on_close:
            #     self.on_close()
            # self.destroy()
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except KeyError as e:
            messagebox.showerror("Empty fields error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))