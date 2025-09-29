import tkinter as tk
from tkinter import messagebox, ttk
from sqlite3 import Error as sqlError
from view.carPopup import CarPopup
from view.tables import Tables
from controllers.carController import get_all_cars, delete_car_by_id, search_car


class CarsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="red")

        self.car_id_var = tk.StringVar()
        self.search_var = tk.StringVar()

        self.func_frame = tk.Frame(self, width=240, bg="blue")
        self.func_frame.pack(side="left", fill="y")
        self.func_frame.pack_propagate(False)

        self.search_label = tk.Label(self.func_frame,
                                     text="Search car",
                                     font=("Arial", 16, "bold")
                                     )
        self.search_label.pack(side="top", fill="x", padx=10, pady=15)
        self.search_entry = tk.Entry(self.func_frame,
                                     textvariable=self.search_var,
                                     font=("Arial", 16, "italic"),
                                     relief="sunken",
                                     bd=3
                                     )

        self.search_entry.pack(side="top", fill="x", padx=10, pady=0)
        self.search_var.trace_add("write", self.search)

        self.add_button = tk.Button(self.func_frame,
                                    height=2,
                                    text="add car",
                                    font=("Arial", 14, "bold"),
                                    bd=8,
                                    command=self.open_add_window)

        self.danger = tk.LabelFrame(self.func_frame,
                                    text="DANGER ZONE",
                                    padx=20,
                                    pady=15,
                                    font=("Arial", 16, "bold"))
        self.danger.pack(side="bottom", fill="x", padx=15, pady=15)
        self.add_button.pack(side="bottom", fill="x", padx=10, pady=15)

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
                                       bd=4,
                                       command=lambda: self.open_add_window(self.entry_id.get()))
        self.update_button.pack(side="left", fill="x", padx=3, pady=15, expand=True)
        self.delete_button = tk.Button(self.f1,
                                       height=2,
                                       text="Delete",
                                       bg="red",
                                       state="disabled",
                                       bd=4,
                                       command=self.confirm_delete)
        self.delete_button.pack(side="left", fill="x", padx=3, pady=15, expand=True)

        self.car_id_var.trace_add("write", self.check_input)

        self.info_frame = tk.Frame(self, bg="green")
        self.info_frame.pack(fill="both", expand=True)
        self.car_data = get_all_cars()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.grid(row=0, column=0, sticky="nsew")

        # вертикальный скролл
        self.vsb = ttk.Scrollbar(self.info_frame, orient="vertical", command=self.table.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.table.configure(yscrollcommand=self.vsb.set)

        # горизонтальный скролл
        self.hsb = ttk.Scrollbar(self.info_frame, orient="horizontal", command=self.table.xview)
        self.hsb.grid(row=1, column=0, sticky="ew")
        self.table.configure(xscrollcommand=self.hsb.set)

        # Настройка растяжки
        self.info_frame.grid_rowconfigure(0, weight=1)
        self.info_frame.grid_columnconfigure(0, weight=1)

    def open_add_window(self, car_id=None):
        self.entry_id.delete(0, tk.END)
        return CarPopup(self, car_id, on_close=self.update_table)

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
                    self.update_table()
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

    def search(self, *args):
        try:
            res = search_car(self.search_var.get().strip())
            if res["qty"] > 0:
                self.car_data = res
                self.table.destroy()
                self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
                self.table.grid(row=0, column=0, sticky="nsew")
                self.vsb.configure(command=self.table.yview)
                self.table.configure(yscrollcommand=self.vsb.set)
                self.hsb.configure(command=self.table.xview)
                self.table.configure(xscrollcommand=self.hsb.set)
            else:
                messagebox.showinfo("Search failed",
                                    f"Value '{self.search_var.get()}' does not exist in Id,"
                                    f" Model, License Plate")
        except sqlError as e:
            messagebox.showerror("Database error", str(e))
        except Exception as e:
            messagebox.showerror("Something went wrong", str(e))

    def update_table(self):
        self.search_entry.delete(0, tk.END)
        self.search_var.set('')
        self.table.destroy()
        self.car_data = get_all_cars()
        self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        self.table.grid(row=0, column=0, sticky="nsew")

        self.vsb.configure(command=self.table.yview)
        self.table.configure(yscrollcommand=self.vsb.set)
        self.hsb.configure(command=self.table.xview)
        self.table.configure(xscrollcommand=self.hsb.set)
