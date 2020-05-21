from tkinter import *
from tkinter import ttk
import tkinter as tk
from src.InitData import InitRandomMatrix, InitPointPosition
from tkinter import messagebox
from functools import partial


root = tk.Tk()
root.title("Tkinter Tab Widgets")
root.minsize(1366, 768)
root.wm_iconbitmap("1.ico")

def click():
    button.configure(bg="red")

button = Button(root, text = "Init Data", activebackground = "pink",activeforeground = "blue", command=click)
button.grid(column= 0, row = 3)
#
#
# list_button = []
# list_button.append(button)
# list_button.append(button)
# list_button.append(button)
# # list_button[0].text = "123"
# # print(list_button[0].text)
#
#
root.mainloop()
#









# import tkinter as tk
#
# window = tk.Tk()
#
# canvas = tk.Canvas(window)
# canvas.pack()
#
# canvas.create_line(0, 0, 200, 100, arrow=tk.LAST) # Or FIRST
#
# window.mainloop()
