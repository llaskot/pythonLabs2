# main_window.py
import tkinter as tk

from view.carsView import CarsView
from view.rentsView import RentView
from view.clientsView import ClientView


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("1200x900")
        self.root.minsize(600, 400)
        self.var = tk.StringVar()
        self.var.set("rent")
        self.setup_widgets()

    def setup_widgets(self):
        self.tabs = tk.Frame(self.root)
        self.tabs.pack(side="top", fill='x')
        self.btn1 = tk.Radiobutton(self.tabs, height=2, text="Rents", variable=self.var, value="rent",
                                   indicatoron=False, command=self.switch_frame)
        self.btn2 = tk.Radiobutton(self.tabs, height=2, text="Cars", variable=self.var, value="car", indicatoron=False,
                                   command=self.switch_frame)
        self.btn3 = tk.Radiobutton(self.tabs, height=2, text="Clients", variable=self.var, value="client",
                                   indicatoron=False, command=self.switch_frame)
        self.btn1.pack(side="left", fill=tk.X, expand=True)
        self.btn2.pack(side="left", fill=tk.X, expand=True)
        self.btn3.pack(side="left", fill=tk.X, expand=True)

        self.frame_holder = RentView(self.root)

        self.frame_holder.pack(side="bottom", fill="both", expand=True)

    def switch_frame(self):
        if self.frame_holder:
            self.frame_holder.destroy()
        print(self.var)
        match self.var.get():
            case "rent":
                self.frame_holder = RentView(self.root)
            case "car":
                self.frame_holder = CarsView(self.root)
            case "client":
                self.frame_holder = ClientView(self.root)
        self.frame_holder.pack(side="bottom", fill="both", expand=True)

    def run(self):
        self.root.mainloop()
