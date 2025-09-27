import tkinter as tk


class RentView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="red")

        self.func_frame = tk.Frame(self, width=350, bg="green")
        self.func_frame.pack(side="left", fill="y")
        self.func_frame.pack_propagate(False)
        # self.add_button = tk.Button(self.func_frame,  height=2 , text="add car", )
        # self.add_button.pack(side="top", fill="x", padx=10, pady=15)

        self.info_frame = tk.Frame(self, bg="green")
        self.info_frame.pack(side="left", fill="both", expand=True)
        # self.car_data = get_all_cars()
        # self.table = Tables(self.info_frame, self.car_data["columns"], self.car_data["values"])
        # self.table.pack(fill="both", expand=True)