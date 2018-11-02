try:
    import tkinter as tk
    import tkinter.ttk as ttk
except ImportError:
    import Tkinter as tk
    import ttk

import matplotlib
matplotlib.use('TkAgg')

from numpy import arange, sin, pi
import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt

class RightFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        


        self.tabController = ttk.Notebook(parent)
        ScatterTab = ttk.Frame(self.tabController)
        self.tabController.add(ScatterTab, text="Scatter")
  
        UnknownTab = ttk.Frame(self.tabController)
        self.tabController.add(UnknownTab, text="Unknown")
        
        BarTab = ttk.Frame(self.tabController)
        self.tabController.add(BarTab, text="Bar")

        self.tabController.grid(row=1, column=2)


        ## DATA
        dataOne = [1, 2, 3, 5, 7, 8]
        dataTwo = [10, 2, 20, 40, 30, 70]
        close = 2
        volume = 3
        
        ## SCATTER
        fig, ax = plt.subplots()
        ax.scatter(dataOne, dataTwo, c='#34D63D', s=volume, alpha=0.5)

        ax.set_title('TK embedded matPLot')
        ax.set_xlabel('x lab')
        ax.set_ylabel('y lab')

        canvas = FigureCanvasTkAgg(fig, master=ScatterTab)
        canvas.draw()
        canvas.get_tk_widget().grid()
        canvas._tkcanvas.grid()
        fig.tight_layout()

        ## BAR
        figBar = Figure(figsize=(5,4), dpi=100)
        axBar = figBar.add_subplot(111)
        data = (20, 35, 30, 35, 27)

        ind = numpy.arange(5)
        width = .5

        rects1 = axBar.bar(ind, data, width)
        canvasBar = FigureCanvasTkAgg(figBar, master=BarTab)
        canvasBar.draw()
        canvasBar.get_tk_widget().grid()
        canvasBar._tkcanvas.grid()
        figBar.tight_layout()


    def packself(self):
        self.grid(row=1, column=2)



        #fig = Figure(figsize=(4, 3), dpi=100)
        #a = fig.add_subplot(111)
        #t = arange(0.0, 3.0, 0.01)
        #s = sin(2*pi*t)

        #a.plot(t, s)
        #a.set_title('TK embedded matPLot')
        #a.set_xlabel('x lab')
        #a.set_ylabel('y lab')