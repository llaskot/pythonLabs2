import tkinter as tk
from sqlite3 import Error as sqlError
from tkinter import messagebox, ttk

from tkcalendar import DateEntry

from controllers.rentController import get_users_list, get_cars_list, prepare_data, save_rent
from view.carPopup import CarPopup
from view.clientPopup import ClientPopup


class RentPopup(tk.Toplevel):
    def __init__(self, master, rent_id=None, on_close=None):
        super().__init__(master)
        self.client_search_var = tk.StringVar(value='')
        self.cars_search_var = tk.StringVar(value='')
        self.valid_year = (self.register(CarPopup.validate_year), "%P")
        self.on_close = on_close
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

        self.date_fraim = tk.LabelFrame(self, text="Terms", padx=5, pady=5)
        self.date_fraim.pack(padx=10, pady=10, fill="x")

        self.date_entry = DateEntry(self.date_fraim)
        self.date_entry.pack(padx=10, pady=10, fill="x", side="left")

        self.term_entry = tk.Entry(self.date_fraim,
                                   validate="key",
                                   validatecommand=self.valid_year)
        self.term_entry.pack(padx=10, pady=10, fill="x", side="left")

        tk.Button(self, text="Cancel", command=self.on_cancel, width=10).pack(pady=10, padx=15, side="left")
        tk.Button(self, text="Save", command=self.on_save, width=10).pack(pady=10, padx=15, side="right")

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
            self.clients = get_users_list(self.client_search_var.get().split(" :")[0].strip())
            self.clients_box['values'] = list(self.clients.keys())
            if len(self.clients_box["values"]) == 0 and " :" not in self.client_search_var.get():
                self.add_client['state'] = "normal"
            else:
                self.add_client['state'] = "disabled"
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))

    def update_car_box(self, *args):
        try:
            self.cars = get_cars_list(self.cars_search_var.get().split(" :: ")[0])
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
            data = prepare_data(self.cars[self.car_box.get()], self.clients[self.clients_box.get()],
                                self.date_entry.get_date(), self.term_entry.get())
            if messagebox.askyesno("Confirm",
                                   f' Check the data before saving. You`ll not be able to change or delete this '
                                   f'document:\n\n'
                                   f'Client ID: {data["client_id"]};\n'
                                   f'Client name: {data["client_name"]};\n'
                                   f'Driver license: {data["client_license"]};\n'
                                   f'Car ID: {data["car_id"]};\n'
                                   f'Car model: {data["car_model"]};\n'
                                   f'License plates: {data["license_plates"]};\n'
                                   f'Start date: {data["start_day"]};\n'
                                   f'Days number: {data["days_number"]};\n'
                                   f'Daily fee: {data["rent_per_day"]};\n'
                                   f'Total rent: {data["rent_total"]};\n'
                                   f'Daily insurance: {data["insurance_per_day"]};\n'
                                   f'Total insurance: {data["insurance_total"]};\n'
                                   f'Total price: {data["total_price"]};'
                                   ):
                save_rent(data["car_id"], data["client_id"], data["days_number"],
                          data["total_price"], data["start_day"])
                messagebox.showinfo("Success", "Successfully saved")
            if self.on_close:
                self.on_close()
            self.destroy()
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except KeyError as e:
            messagebox.showerror("Empty fields error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))
