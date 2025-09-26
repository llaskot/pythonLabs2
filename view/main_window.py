# main_window.py
import tkinter as tk

from view.carsView import CarsView


class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Main Window")
        self.root.geometry("1200x900")
        self.root.minsize(600, 400)
        self.var = tk.StringVar()
        self.var.set("1")
        self.setup_widgets()


    def setup_widgets(self):
        self.tabs = tk.Frame(self.root)
        self.tabs.pack(side="top", fill='x')
        self.btn1 = tk.Radiobutton(self.tabs, height=2 , text="Button 1", variable=self.var, value="1", indicatoron=False)
        self.btn2 = tk.Radiobutton(self.tabs, height=2 ,text="Button 2", variable=self.var, value="2", indicatoron=False)
        self.btn3 = tk.Radiobutton(self.tabs, height=2 ,text="Button 3", variable=self.var, value="3", indicatoron=False)
        self.btn1.pack(side="left",fill=tk.X, expand=True)
        self.btn2.pack(side="left",fill=tk.X, expand=True)
        self.btn3.pack(side="left",fill=tk.X, expand=True)
        self.frame_holder = CarsView(self.root)
        # self.frame_holder.pack(side="bottom", fill="both", expand=True)


        self.frame_holder.pack(side="bottom", fill="both", expand=True)

    def run(self):
        self.root.mainloop()
