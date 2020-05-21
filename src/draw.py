from src.init_data import init_line_points
import tkinter as tk


def draw_line(canvas, list_position, data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                line_points = init_line_points(list_position[i], list_position[j])
                canvas.create_line(line_points[0][0], line_points[0][1], line_points[1][0], line_points[1][1],
                                   arrow=tk.LAST, tags="all_line_tag")  # Or FIRST, dash = (3, 3), fill="red"


def draw_bestline(a, canvas, list_position):
    for i in range(1, len(a), 1):
        line_points = init_line_points(list_position[a[i-1]], list_position[a[i]])
        canvas.create_line(line_points[0][0], line_points[0][1], line_points[1][0], line_points[1][1],
                                   arrow=tk.LAST, tags="best_line_tag", fill='red')


