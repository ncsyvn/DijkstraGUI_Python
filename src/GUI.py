from tkinter import *
from tkinter import ttk
import tkinter as tk
from src.InitData import InitRandomMatrix, InitPointPosition, InitLinePoints
from tkinter import messagebox
from functools import partial


root = tk.Tk()
root.title("Tkinter Tab Widgets")
root.minsize(1366,768)
root.wm_iconbitmap("1.ico")

amount_point_var = None
amount_relationship_var = None
data = None
list_position = None
choose_point = [-1, -1]

check_click = False
"""
    Tab 1:
        Tab 1 is Input amount of point and relationship each double point
"""

def submit_command():

    global amount_point_var, amount_relationship_var, data, list_position, check_click, canvas
    amount_point_var = int(amount_point_text_input.get())
    amount_relationship_var = int(amount_relationship_text_input.get())
    if amount_point_var*amount_point_var-amount_point_var < amount_relationship_var:
        messagebox.showwarning("Warning", "Amount of relationship too large")
    else:
        data = InitRandomMatrix(amount_point_var, amount_relationship_var)
        list_position = InitPointPosition(amount_point_var)
        for i in range(len(list_position)):
            button = Button(root.graph_tab, text="Point "+str(i+1), activebackground="pink", activeforeground="blue",
                            width=6, command=partial(choose_point_command, i))\
                .place(x=list_position[i][0], y=list_position[i][1])
        draw_line()
        print(list_position)



    labelFrame1 = LabelFrame(root.init_data_tab, text = "Data after init")
    labelFrame1.grid(column=2, row=0, padx=0, pady=0)
    if amount_point_var <= 10:
        width_column = 10
    elif amount_point_var <= 20:
        width_column = 6
    else:
        width_column = 4
    for i in range(amount_point_var):  # Rows
        for j in range(amount_point_var):  # Columns
            b = Entry(labelFrame1, width=width_column)
            b.insert(0, data[i][j])
            b.grid(row=i, column=j)


def choose_point_command(a):
    global canvas
    if choose_point[0] == -1 and choose_point[1] == -1:
        choose_point[0] = a
    elif choose_point[0] != -1 and choose_point[1] == -1:
        choose_point[1] = a
    elif choose_point[0] != -1 and choose_point[1] != -1:
        choose_point[0] = a
        choose_point[1] = -1
    canvas.create_line(0, 0, 500, 100, arrow=tk.LAST) # Or FIRST

    print(choose_point)





# Init 2 tab
tabControl = ttk.Notebook(root)
root.init_data_tab = ttk.Frame(tabControl)
tabControl.add(root.init_data_tab, text = "Init Data Tab")

root.graph_tab = ttk.Frame(tabControl)
tabControl.add(root.graph_tab, text = "Graph Tab")
tabControl.pack(expand = 1, fill = "both")

canvas = tk.Canvas(root.graph_tab, bg='gray') # Color of tab
canvas.pack(side="left", fill="both", expand=True)



# Init components in tab
# Tab 1
labelFrame = LabelFrame(root.init_data_tab, text = "Input")
labelFrame.grid(column=0, row=0, padx=8, pady=4)

amount_point_label = Label(labelFrame, text = "Enter Amount of Point:")
amount_point_label.grid(column=0, row=0, sticky='W')

amount_point_text_input = Entry(labelFrame, width = 20)
amount_point_text_input.grid(column = 1, row = 0)

amount_relationship_label = Label(labelFrame, text = "Enter Amount of Relationship:")
amount_relationship_label.grid(column = 0, row = 1)

amount_relationship_text_input = Entry(labelFrame, width = 20)
amount_relationship_text_input.grid(column= 1, row = 1)

submit_button = Button(labelFrame, text = "Init Data", activebackground = "pink",
                          activeforeground = "blue", command=submit_command, width=6)
submit_button.grid(column= 0, row = 3)

# Tab 2
labelFrameTab2 = LabelFrame(canvas, text="Mode On/Off")
labelFrameTab2.pack(padx=10, pady=20, anchor='nw')

def hide_all_line():
    global canvas, button_off_all_line
    if button_off_all_line['text'] == "Hide all line":
        canvas.delete("my_tag")
        button_off_all_line.configure(bg="blue", text="Show all line")
    else:
        draw_line()
        button_off_all_line.configure(bg="gray", text="Hide all line")

button_off_all_line = Button(labelFrameTab2, text="Hide all line...", command=hide_all_line)
button_off_all_line.pack(pady=3, padx=5,  anchor="nw")

button_off_best_line = Button(labelFrameTab2, text="Hide best line", command=hide_all_line)
button_off_best_line.pack(pady=8, padx=5,  anchor="nw")



def draw_line():
    global data, list_position
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                line_points = InitLinePoints(list_position[i], list_position[j])
                canvas.create_line(line_points[0][0], line_points[0][1], line_points[1][0], line_points[1][1],
                                   arrow=tk.LAST, tags="my_tag")  # Or FIRST, dash = (3, 3), fill="red"



root.mainloop()

