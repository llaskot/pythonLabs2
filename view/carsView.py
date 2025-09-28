import tkinter as tk

from view.carPopup import CarPopup
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
        self.danger = tk.LabelFrame(self.func_frame, text="DANGER ZONE")
        self.danger.pack(side="bottom", fill="x", padx=10, pady=15)
        self.label_id = tk.Label(self.danger, text="Car ID")
        self.label_id.pack(side="left", fill="x", padx=10, pady=15)
        self.valid_id = (self.register(CarPopup.validate_year), "%P")
        self.entry_id = tk.Entry(self.danger, validate="key", validatecommand=self.valid_id)
        self.entry_id.pack(side="left", fill="x", padx=10, pady=15)
        self.update_button = tk.Button(self.danger, height=2, text="Update",
                                       command=lambda: self.open_add_window(int(self.entry_id.get())))
        self.update_button.pack(side="top", fill="x", padx=10, pady=15)

        self.info_frame = tk.Frame(self, bg="green")
        self.info_frame.pack(side="left", fill="both", expand=True)
        self.car_data = get_all_cars()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.pack(fill="both", expand=True)
        # self.availability_status = tk.IntVar(value=0)

    def open_add_window(self, car_id = None):
        return CarPopup(self, car_id)
