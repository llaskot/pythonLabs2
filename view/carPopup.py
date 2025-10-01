import re
from sqlite3 import Error as sqlError
import tkinter as tk
from tkinter import messagebox
from controllers.carController import create_car, get_car_by_id


class CarPopup(tk.Toplevel):
    def __init__(self, master, car_id=None, on_close=None):
        self.on_close = on_close
        super().__init__(master)
        self.car_id = car_id
        self.availability_status = tk.IntVar(value=1)
        self.title("Add new car" if not car_id else f"Update the car # {car_id}")
        self.geometry("500x350")
        self.valid_year = (self.register(self.validate_year), "%P")
        self.valid_price = (self.register(self.validate_price), "%P")

        self.name = tk.LabelFrame(self, text="Car model", padx=5, pady=5)
        self.name.pack(padx=10, pady=1, fill="x")
        self.model_entry = tk.Entry(self.name)
        self.model_entry.pack(pady=5, fill="x")

        self.f1 = tk.Frame(self)
        self.f1.pack(fill="x")

        self.year = tk.LabelFrame(self.f1, text="Car year", padx=5, pady=5)
        self.year.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        self.year_entry = tk.Entry(self.year, validate="key", validatecommand=self.valid_year)
        self.year_entry.pack(pady=5, fill="x")

        self.color = tk.LabelFrame(self.f1, text="Car color", padx=5, pady=5)
        self.color.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        self.color_entry = tk.Entry(self.color)
        self.color_entry.pack(pady=5, fill="x")

        self.lic = tk.LabelFrame(self, text="License plate", padx=5, pady=5)
        self.lic.pack(padx=10, pady=1, fill="x")
        self.lic_entry = tk.Entry(self.lic)
        self.lic_entry.pack(pady=5, fill="x")

        self.f2 = tk.Frame(self)
        self.f2.pack(fill="x")
        self.price = tk.LabelFrame(self.f2, text="Daily Price", padx=5, pady=5)
        self.price.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        self.price_entry = tk.Entry(self.price, validate="key", validatecommand=self.valid_price)
        self.price_entry.pack(pady=5, fill="x")
        self.insurance = tk.LabelFrame(self.f2, text="Insurance Price", padx=5, pady=5)
        self.insurance.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        self.insurance_entry = tk.Entry(self.insurance, validate="key", validatecommand=self.valid_price)
        self.insurance_entry.pack(pady=5, fill="x")
        self.availability = tk.LabelFrame(self.f2, text="Availability", padx=5, pady=5)
        self.availability.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        self.radio_yes = tk.Radiobutton(self.availability, text="Yes", variable=self.availability_status, value=1)
        self.radio_no = tk.Radiobutton(self.availability, text="No", variable=self.availability_status, value=0)
        self.radio_yes.pack(side="left")
        self.radio_no.pack(side="left")
        tk.Button(self, text="Cancel", command=self.on_cancel, width=10).pack(pady=10, padx=15, side="left")
        tk.Button(self, text="Save", command=self.on_save, width=10).pack(pady=10, padx=15, side="right")
        if self.car_id:
            self.fill_in()

    # validation
    @classmethod
    def validate_year(cls, val):
        return (val.isdigit() or val == "") and len(val) <= 4

    @classmethod
    def validate_price(cls, val):
        if val == "":
            return True
        if not re.fullmatch(r"\d*\.?\d{0,2}", val):
            return False
        return True

    def on_cancel(self):
        if self.on_close:
            self.on_close()
        self.destroy()

    def on_save(self):
        vals = (self.car_id,
                self.model_entry.get(),
                self.year_entry.get(),
                self.color_entry.get(),
                self.lic_entry.get(),
                self.price_entry.get(),
                self.insurance_entry.get(),
                self.availability_status.get())

        try:
            create_car(vals)
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

    def fill_in(self):
        try:
            car = get_car_by_id(self.car_id)["values"][0]
            self.model_entry.insert(0, car[1])
            self.color_entry.insert(0, car[3])
            self.year_entry.insert(0, str(car[2]))
            self.lic_entry.insert(0, car[4])
            self.price_entry.insert(0, str(car[5]))
            self.insurance_entry.insert(0, str(car[6]))
            self.availability_status.set(car[7])
        except Exception as e:
            self.on_cancel()
            messagebox.showerror("Something went wrong", str(e) + "\nMay by this car doesn't exist?")
