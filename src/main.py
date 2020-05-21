from tkinter import *
from tkinter import ttk
import tkinter as tk
from src.init_data import init_random_matrix, init_point_position
from tkinter import messagebox
from functools import partial
from src.config import point_color, point_color_choose
from src.dijkstra_algorithm import dijkstra
from src.draw import draw_bestline, draw_line

root = tk.Tk()                     # Create new Tkinter
root.title("Tkinter Tab Widgets")  # Set title
root.minsize(1366, 768)            # Customize size
root.wm_iconbitmap("1.ico")        # Set icon

""" Define global variables """
amount_point_var = None         # Amount of point, get from text field input
amount_relationship_var = None  # Amount of relationship, get from text field input
data = None                     # Matrix relationship of all points
list_position = None            # List of coordinate's point to draw on canvas
choose_point = [-1, -1]         # Contain 2 point to find best line base on dijkstra algorithm
list_point = []                 # Handling all point (button) to change color when click
best_line = None                # Dict contain path from first to second point. Ex: {distance: "13", 'path': [0, 4, 2]

"""
    Init 2 tab:
        Tab 1 is init_data_tab to input amount of point and amount of relationship and init matrix relationship
        Tab 2 is graph_data to draw and user can find best line of 2 points.
    Init canvas link tab2 to handle line and button.
"""
tabControl = ttk.Notebook(root)
# Tab 1
root.init_data_tab = ttk.Frame(tabControl)
tabControl.add(root.init_data_tab, text="Init Data Tab")
# Tab2
root.graph_tab = ttk.Frame(tabControl)
tabControl.add(root.graph_tab, text="Graph Tab")
tabControl.pack(expand=1, fill="both")
# Canvas
canvas = tk.Canvas(root.graph_tab, bg='gray') # Color of tab
canvas.pack(side="left", fill="both", expand=True)


""" 
    Init components in tab
"""
# Components on tab 1
labelFrame = LabelFrame(root.init_data_tab, text="Input")
labelFrame.grid(column=0, row=0, padx=8, pady=4)

amount_point_label = Label(labelFrame, text = "Enter Amount of Point:")
amount_point_label.grid(column=0, row=0, sticky='W')

amount_point_text_input = Entry(labelFrame, width=20)  # Entry is a textfield to input amount of point
amount_point_text_input.grid(column=1, row=0)

amount_relationship_label = Label(labelFrame, text="Enter Amount of Relationship:")
amount_relationship_label.grid(column=0, row=1)

amount_relationship_text_input = Entry(labelFrame, width=20)  # Entry is a textfield to input amount of relationship
amount_relationship_text_input.grid(column=1, row=1)

# Components on tab 2
labelFrameTab2 = LabelFrame(canvas, text="Mode On/Off")
labelFrameTab2.pack(padx=10, pady=20, anchor='nw')


def submit_command():
    """
        Event of submit button
        When user click to submit button:
            1. Init matrix relationship data with n*n dimension
            2. Create list position of points base on coordinate
            3. Draw matrix relationship on tab to view
            4. Draw point and line of two points which have relationship
    :return:
    """
    global amount_point_var, amount_relationship_var, data, list_position, canvas, list_point
    amount_point_var = int(amount_point_text_input.get())
    amount_relationship_var = int(amount_relationship_text_input.get())
    if amount_point_var*amount_point_var-amount_point_var < amount_relationship_var:
        messagebox.showwarning("Warning", "Amount of relationship too large")
    else:
        """ Init data """
        data = init_random_matrix(amount_point_var, amount_relationship_var)
        list_position = init_point_position(amount_point_var)

        """ Draw button """
        for i in range(len(list_position)):
            list_point.append(Button(canvas, text="Point "+str(i+1), activebackground="pink", activeforeground="blue",
                            width=6, command=partial(choose_point_command, i), bg=point_color))
            list_point[i].place(x=list_position[i][0], y=list_position[i][1])

        """ Draw line """
        draw_line(canvas, list_position, data)
        print(list_position)

    """ Draw matrix """
    labelFrame1 = LabelFrame(root.init_data_tab, text="Data after init")
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


""" Button submit to init data """
submit_button = Button(labelFrame, text="Init Data", activebackground="pink",
                       activeforeground="blue", command=submit_command, width=6)
submit_button.grid(column=0, row=3)


def choose_point_command(a):
    """
        Event of choose point button
        Handling to make sure user choose 2 point to find best line
        After choose 2 points, fine best line and draw it on canvas
    :param a:
    :return:
    """
    global canvas, best_line
    if choose_point[0] != a and choose_point[1] != a:  # if a was not be choose
        if choose_point[0] == -1 and choose_point[1] == -1:
            choose_point[0] = a
            list_point[a].configure(bg=point_color_choose)  # Change color of point
        elif choose_point[0] != -1 and choose_point[1] == -1:
            choose_point[1] = a
            list_point[a].configure(bg=point_color_choose)
            best_line = dijkstra(data, amount_point_var, choose_point[0], choose_point[1])  # Find best line
            if best_line is not None:
                print(best_line)
                draw_bestline(best_line["path"], canvas, list_position)  # Draw best line with difference color
            else:
                print(best_line)
        elif choose_point[0] != -1 and choose_point[1] != -1:
            list_point[choose_point[0]].configure(bg=point_color)
            list_point[choose_point[1]].configure(bg=point_color)
            choose_point[0] = a
            choose_point[1] = -1  # Uncheck
            list_point[a].configure(bg=point_color_choose)
            canvas.delete("best_line_tag")
    elif choose_point[0] == a:
        if choose_point[1] == -1:
            choose_point[0] = -1  # Uncheck
            list_point[a].configure(bg=point_color)
        else:
            choose_point[1] = -1  # Uncheck
            list_point[a].configure(bg=point_color)
            canvas.delete("best_line_tag")  # delete best line to refresh
    elif choose_point[1] == a:
        list_point[a].configure(bg=point_color)
        choose_point[1] = -1
        canvas.delete("best_line_tag")  # delete best line to refresh

    print(choose_point)


def hide_all_line():
    """
        Event of off_all_line button
        Function to show or hide all lines off all points (keep hose best line with 2 point)
    :return:
    """
    global canvas, button_off_all_line, best_line
    if button_off_all_line['text'] == "Hide all line":                  # If current status is show and want to hide
        canvas.delete("all_line_tag")                                   # Delete all lines from canvas
        button_off_all_line.configure(bg="blue", text="Show all line")  # Change status of button
    else:                                                               # If current status is hide and want to show
        draw_line(canvas, list_position, data)                          # Draw new all line
        if best_line is not None:                                       # If best line is not none, draw best line
            draw_bestline(best_line["path"], canvas, list_position)
        button_off_all_line.configure(bg="gray", text="Hide all line")


""" Button handling on/off all line"""
button_off_all_line = Button(labelFrameTab2, text="Hide all line", command=hide_all_line)
button_off_all_line.pack(pady=3, padx=5,  anchor="nw")


def hide_all_bestline():
    """
        Event of off_best_line button
        Function to show or hide best lines of 2 points
    :return:
    """
    global canvas, button_off_best_line, best_line
    if best_line is not None:
        if button_off_best_line['text'] == "Hide best line":                  # If current status is show and want to hide
            canvas.delete("best_line_tag")                                    # Delete best lines from canvas
            button_off_best_line.configure(bg="blue", text="Show best line")  # Change status of button
        else:                                                                 # If current status is hide and want to show
            draw_line(canvas, list_position, data)                            # Draw new best line
            if best_line is not None:                                         # If best line is not none, draw best line
                draw_bestline(best_line["path"], canvas, list_position)
            button_off_best_line.configure(bg="gray", text="Hide best line")


""" Button handling on/off best line """
button_off_best_line = Button(labelFrameTab2, text="Hide best line", command=hide_all_bestline)
button_off_best_line.pack(pady=8, padx=5,  anchor="nw")


# Play ...
root.mainloop()

