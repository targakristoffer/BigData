try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk

class Button_run(ttk.Button):
    def __init__(self, parent, guiFunction, row, column, default_text="Kjør"):
        super().__init__(parent, text=default_text, command=guiFunction)
        theme = ttk.Style()


        theme.configure(self.winfo_class(), padding=6, background="#fff", foreground="#b34")
        
        self.grid(row=row, column=column)

     
    def add(self):
        print('asda')