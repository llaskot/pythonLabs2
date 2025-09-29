from tkinter import ttk


class Tables(ttk.Treeview):
    def __init__(self, parent, columns: list, vals: [tuple]):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Custom.Treeview",
                        rowheight=38,
                        font=("Arial", 12),
                        padding=(10, 10, 10, 10),
                        )
        style.configure("Custom.Treeview.Heading",
                        relief="raised",
                        bg="yellow",
                        borderwidth=1,
                        font=("Arial", 12, "bold"),
                        )
        super().__init__(parent, columns=columns, show="headings", style="Custom.Treeview")
        self.data = self.get_data(columns, vals)
        self.sort_reverse = {col: False for col in columns}
        for col in columns:
            self.heading(col,
                         text=self.fix_column_name(col),
                         command=lambda c=col: self.sort_by_column(c))
            self.column(col, anchor="center", stretch=True, width=1, minwidth=100,)
        self.set_vals()

    @classmethod
    def get_data(cls, columns, vals):
        return [cls.get_row(columns, val) for val in vals]

    @classmethod
    def get_row(cls, col_name, values):
        return {key: val for key, val in zip(col_name, values)}

    @classmethod
    def fix_column_name(cls, name):
        return " ".join(word.capitalize() for word in name.split("_"))

    def set_vals(self):
        for row in self.data:
            self.insert("", "end", values=list(row.values()))

    def sort_by_column(self, col):
        self.data.sort(key=lambda x: x[col], reverse=self.sort_reverse[col])
        self.sort_reverse[col] = not self.sort_reverse[col]
        self.delete(*self.get_children())
        self.set_vals()

    # if __name__ == "__main__":
#     Tables.get_data(["a", "b", "c"], [(1, 2, 3), (4, 5, 3)])
