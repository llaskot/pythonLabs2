from tkinter import ttk
import tkinter as tk


class CarsView(tk.Frame):
    pass



# class Tables(ttk.Treeview):
#     def __init__(self, parent, columns: list, vals: [tuple]):
#         style = ttk.Style()
#         style.configure("Custom.Treeview",
#                         rowheight=38,
#                         font=("Arial", 12),
#                         padding=(10,10,10,10),
#                         )
#         super().__init__(parent, columns=columns, show="headings", style="Custom.Treeview")
#         for col in columns:
#             self.heading(col, text=col)
#             self.column(col, anchor="center")
#         self.set_vals(vals)
#
#     def set_vals(self, vals: [tuple]):
#         for row in vals:
#             self.insert("", "end", values=row)




# tree.heading("col1", text="Column 1")
# tree.heading("col2", text="Column 2")
