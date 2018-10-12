try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk

class Button_tweet(ttk.Button):
    def __init__(self, parent, guiFunction, row, column, default_text="Hent"):
        super().__init__(parent, text=default_text, command=guiFunction, width=100)
        theme = ttk.Style()
        

        theme.configure(self.winfo_class(), padding=6, background="#FFF", foreground="#DF34DF", font=("Helvitca", 12))
        
        self.grid(row=row, column=column, padx=2.5, pady=2.5)

     
    def add(self):
        print('asda')