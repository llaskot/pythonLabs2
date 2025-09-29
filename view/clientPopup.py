import tkinter as tk
class ClientPopup(tk.Toplevel):
    def __init__(self,master, client_id=None,  on_close=None):
        super().__init__(master)
        self.on_close = on_close
        self.client_id = client_id
        self.title("Add new client" if not client_id else f"Update the client # {client_id}")
        self.geometry("500x350")
        self.name = tk.LabelFrame(self, text="Client fullname", padx=5, pady=5)
        self.name.pack(padx=10, pady=1, fill="x")
        self.model_entry = tk.Entry(self.name)
        self.model_entry.pack(pady=5, fill="x")