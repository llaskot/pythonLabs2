# main_window.py
import tkinter as tk
from view.carsView import CarsView
from view.rentsView import RentView
from view.clientsView import ClientView
from view.statistics import Statistics, StatisticsFrame


class MainWindow:
    def __init__(self):
        root = self._create_root()
        tabs_holder = self._create_tabs_holder(root)
        self._create_frame_holder(root)
        self._create_tabs(tabs_holder)

    def _create_tabs(self, parent):
        self.var = tk.StringVar()
        self.var.set("rent")
        self.btn1 = tk.Radiobutton(parent, height=2, text="Rents", variable=self.var, value="rent",
                                   indicatoron=False, command=self.switch_frame)
        self.btn2 = tk.Radiobutton(parent, height=2, text="Cars", variable=self.var, value="car", indicatoron=False,
                                   command=self.switch_frame)
        self.btn3 = tk.Radiobutton(parent, height=2, text="Clients", variable=self.var, value="client",
                                   indicatoron=False, command=self.switch_frame)
        self.btn1.pack(side="left", fill=tk.X, expand=True)
        self.btn2.pack(side="left", fill=tk.X, expand=True)
        self.btn3.pack(side="left", fill=tk.X, expand=True)

    def _create_root(self):
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("1200x900")
        self.root.minsize(600, 400)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def _create_tabs_holder(self, root):
        self.tabs = tk.Frame(root)
        self.tabs.pack(side="top", fill='x')

    def _create_frame_holder(self, root):
        self.frame_holder = RentView(root)
        self.frame_holder.pack(side="bottom", fill="both", expand=True)

    def switch_frame(self):
        if self.frame_holder:
            self.frame_holder.destroy()
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

    def on_close(self):
        from connection import connection
        if connection:
            connection.close()
        self.root.destroy()
