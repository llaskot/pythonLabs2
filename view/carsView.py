import tkinter as tk
from tkinter import messagebox
from wsgiref.validate import check_input

from view.carPopup import CarPopup
from view.tables import Tables
from controllers.carController import get_all_cars, delete_car_by_id


class CarsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="red")

        self.func_frame = tk.Frame(self, width=350, bg="blue")
        self.func_frame.pack(side="left", fill="y")
        self.func_frame.pack_propagate(False)
        self.add_button = tk.Button(self.func_frame, height=2, text="add car", command=self.open_add_window)
        self.add_button.pack(side="top", fill="x", padx=10, pady=15)
        self.car_id_var = tk.StringVar()


        self.danger = tk.LabelFrame(self.func_frame,
                                    text="DANGER ZONE",
                                    padx=50,
                                    pady=15,
                                    font=("Arial", 16, "bold"))
        self.danger.pack(side="bottom", fill="x", padx=15, pady=15)

        self.f0 = tk.Frame(self.danger)
        self.f0.pack(fill="x", side="top")

        self.label_id = tk.Label(self.f0, text="Car ID")
        self.label_id.pack(side="left", fill="x", padx=10, pady=15, expand=True)

        self.valid_id = (self.register(CarPopup.validate_year), "%P")
        self.entry_id = tk.Entry(self.f0,
                                 validate="key",
                                 textvariable=self.car_id_var,
                                 validatecommand=self.valid_id)
        self.entry_id.pack(side="left", fill="x", padx=10, pady=15, expand=True)

        self.f1 = tk.Frame(self.danger)
        self.f1.pack(fill="x", side="bottom")
        self.update_button = tk.Button(self.f1,
                                       height=2,
                                       text="Update",
                                       bg="orange",
                                       state="disabled",
                                       command=lambda: self.open_add_window(self.entry_id.get()))
        self.update_button.pack(side="left", fill="x", padx=10, pady=15, expand=True)
        self.delete_button = tk.Button(self.f1,
                                       height=2,
                                       text="Delete",
                                       bg="red",
                                       state="disabled",
                                       command=self.confirm_delete)
        self.delete_button.pack(side="left", fill="x", padx=10, pady=15, expand=True)
        self.car_id_var.trace_add("write", self.check_input)

        self.info_frame = tk.Frame(self, bg="green")
        self.info_frame.pack(side="left", fill="both", expand=True)
        self.car_data = get_all_cars()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.pack(fill="both", expand=True)

    def open_add_window(self, car_id=None):
        self.entry_id.delete(0, tk.END)
        return CarPopup(self, car_id)

    def delete_car(self):
        try:
            return delete_car_by_id(self.entry_id.get())
        except Exception as e:
            raise e

    def confirm_delete(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to delete?"):
            try:
                res = self.delete_car()
                self.entry_id.delete(0, tk.END)
                if res["success"] and res["affected_rows"] > 0:
                    messagebox.showinfo("Success", "Successfully deleted")
                else:
                    messagebox.showerror("Something went wrong", "Looks like there is nothing to delete")
            except Exception as e:
                messagebox.showerror("Something went wrong", str(e) + "\nMay by this car doesn't exist?")

    def check_input(self, *args):
        if self.entry_id.get().strip():
            self.delete_button.config(state="normal")
            self.update_button.config(state="normal")
        else:
            self.delete_button.config(state="disabled")
            self.update_button.config(state="disabled")
