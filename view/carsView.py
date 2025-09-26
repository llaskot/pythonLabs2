import tkinter as tk

from view.tables import Tables


class CarsView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="red")

        self.func_frame = tk.Frame(self, width=350, bg="blue")
        self.func_frame.pack(side="left", fill="y")
        self.func_frame.pack_propagate(False)
        self.add_button = tk.Button(self.func_frame,  height=2 , text="add car", )
        self.add_button.pack(side="top", fill="x", padx=10, pady=15)

        self.info_frame = tk.Frame(self, bg="green")
        self.info_frame.pack(side="left", fill="both", expand=True)
        self.table = Tables(self.info_frame, ['col1', 'col2'], [(1, 'aa'), (2, 'bb'), (3, 'cc')])
        self.table.pack(fill="both", expand=True)

