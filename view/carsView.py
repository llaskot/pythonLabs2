import tkinter as tk

from view.tables import Tables
from controllers.carController import get_all_cars


class CarsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="red")

        self.func_frame = tk.Frame(self, width=350, bg="blue")
        self.func_frame.pack(side="left", fill="y")
        self.func_frame.pack_propagate(False)
        self.add_button = tk.Button(self.func_frame, height=2, text="add car", command=self.open_add_window)
        self.add_button.pack(side="top", fill="x", padx=10, pady=15)

        self.info_frame = tk.Frame(self, bg="green")
        self.info_frame.pack(side="left", fill="both", expand=True)
        self.car_data = get_all_cars()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.pack(fill="both", expand=True)
        self.availability_status = tk.IntVar(value=0)

    def open_add_window(self):
        popup = tk.Toplevel(self)
        popup.title("Add new car")
        popup.geometry("500x350")

        name = tk.LabelFrame(popup, text="Car model", padx=5, pady=5)
        name.pack(padx=10, pady=1, fill="x")
        model_entry = tk.Entry(name)
        model_entry.pack(pady=5, fill="x")

        f1 = tk.Frame(popup)
        f1.pack(fill="x")

        year = tk.LabelFrame(f1, text="Car year", padx=5, pady=5)
        year.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        year_entry = tk.Entry(year)
        year_entry.pack(pady=5, fill="x")

        color = tk.LabelFrame(f1, text="Car color", padx=5, pady=5)
        color.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        color_entry = tk.Entry(color)
        color_entry.pack(pady=5, fill="x")

        lic = tk.LabelFrame(popup, text="License plate", padx=5, pady=5)
        lic.pack(padx=10, pady=1, fill="x")
        lic_entry = tk.Entry(lic)
        lic_entry.pack(pady=5, fill="x")

        f2 = tk.Frame(popup)
        f2.pack(fill="x")

        price = tk.LabelFrame(f2, text="Daily Price", padx=5, pady=5)
        price.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        price_entry = tk.Entry(price)
        price_entry.pack(pady=5, fill="x")

        insurance = tk.LabelFrame(f2, text="Insurance Price", padx=5, pady=5)
        insurance.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        insurance_entry = tk.Entry(insurance)
        insurance_entry.pack(pady=5, fill="x")

        # f3 = tk.Frame(popup)
        # f3.pack(fill="x")
        availability = tk.LabelFrame(f2, text="Availability", padx=5, pady=5)
        availability.pack(padx=10, pady=1, side="left", fill="x", expand=True)
        radio_yes = tk.Radiobutton(availability, text="Yes", variable=self.availability_status, value=1)
        radio_no = tk.Radiobutton(availability, text="No", variable=self.availability_status, value=0)
        radio_yes.pack(side="left")
        radio_no.pack(side="left")


        tk.Button(popup, text="Submit", command= self.on_submit(insurance_entry, popup)).pack(pady=10)

    def on_submit(self, entry, popup):
        print("Entered:", entry.get())
        popup.destroy()
