try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk


class RightTextView(tk.Text):
    def __init__(self, parent, setHeight, setWidth):
        super().__init__(parent, height=setHeight, width=setWidth)

    def remove(self):
        self.delete('1.0', 'end')

    def fill(self, text):
        self.insert('1.0', text)

    def packself(self):
        self.grid(row=1, column=2)