from tkinter.filedialog import *
import tkinter as tk
from bl.text import Text

canvas = tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg = "white")

top = Frame(canvas)
top.pack(padx = 10, pady = 5, anchor ='nw')

b1 = Button(canvas, Text = "Open", bg = "white")
b1.pack(in_ = top, side=LEFT)

b2 = Button(canvas, Text = "Save", bg = "white")
b2.pack(in_ = top, side=LEFT)

b3 = Button(canvas, text = "Clear", bg = "white")
b3.pack(in_ = top, side=LEFT)

b4 = Button(canvas, text = "Exit", bg = "white")
b4.pack(in_ = top, side=LEFT)

canvas.mainloop()
