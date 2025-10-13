import tkinter as tk


class StatisticsFrame(tk.Frame):
    pass


class Statistics:
    def __init__(self, parent_tk: tk.Tk):
        self._tk = parent_tk

    @property
    def frame(self):
        return StatisticsFrame(self._tk)

    @property
    def tab_button(self, parent, tk_var, function):
        return tk.Radiobutton(parent, height=2, text="Clients", variable=tk_var, value="client",
                              indicatoron=False, command=function)
