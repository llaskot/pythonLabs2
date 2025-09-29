import tkinter as tk
from tkinter import messagebox
from sqlite3 import Error as sqlError

from controllers.clientController import create_client, get_client_by_id


class ClientPopup(tk.Toplevel):
    def __init__(self, master, client_id=None, on_close=None):
        super().__init__(master)
        self.on_close = on_close
        self.client_id = client_id
        self.title("Add new client" if not client_id else f"Update the client # {client_id}")
        self.geometry("500x350")
        self.name = tk.LabelFrame(self, text="Client fullname", padx=5, pady=5)
        self.name.pack(padx=10, pady=1, fill="x")
        self.model_entry = tk.Entry(self.name)
        self.model_entry.pack(pady=5, fill="x")

        self.license = tk.LabelFrame(self, text="License Number", padx=5, pady=5)
        self.license.pack(padx=10, pady=1, fill="x")
        self.license_entry = tk.Entry(self.license)
        self.license_entry.pack(pady=5, fill="x")
        tk.Button(self, text="Cancel", command=self.on_cancel).pack(pady=10, padx=15, side="left")
        tk.Button(self, text="Save", command=self.on_save).pack(pady=10, padx=15, side="right")
        if self.client_id:
            self.fill_in()

    def on_cancel(self):
        if self.on_close:
            self.on_close()
        self.destroy()

    def on_save(self):
        vals = (self.client_id,
                self.model_entry.get(),
                self.license_entry.get()
                )
        try:
            create_client(vals)
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
            car = get_client_by_id(self.client_id)["values"][0]
            self.model_entry.insert(0, car[1])
            self.license_entry.insert(0,car[2])
        except Exception as e:
            self.on_cancel()
            messagebox.showerror("Something went wrong", str(e) + "\nMay by this client doesn't exist?")
