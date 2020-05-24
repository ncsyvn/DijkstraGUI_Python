import tkinter as tk
import math
from src.config import best_line_color, all_line_tag, best_line_tag, label_bg_color, \
    label_fg_color, label_best_bg_color, label_best_fg_color
from src.init_data import init_line_points
from tkinter import *

def draw_line(canvas, list_position, data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                line_points = init_line_points(list_position[i], list_position[j])
                canvas.create_line(line_points[0][0], line_points[0][1], line_points[1][0], line_points[1][1],
                                   arrow=tk.LAST, tags=all_line_tag)  # Or FIRST, dash = (3, 3), fill="red"


def draw_bestline(a, canvas, list_position):
    for i in range(1, len(a), 1):
        line_points = init_line_points(list_position[a[i-1]], list_position[a[i]])
        canvas.create_line(line_points[0][0], line_points[0][1], line_points[1][0], line_points[1][1],
                                   arrow=tk.LAST, tags=best_line_tag, fill=best_line_color, width=2)


def draw_distance(data, canvas, list_position, k):
    list_distance_label = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != 0:
                line_points = init_line_points(list_position[i], list_position[j])
                distance = math.sqrt((line_points[0][0]-line_points[1][0]) * (line_points[0][0]-line_points[1][0]) \
                           + (line_points[0][1]-line_points[1][1]) * (line_points[0][1]-line_points[1][1]))
                if distance < 300:
                    vector = [(line_points[1][0]-line_points[0][0])*k*3, (line_points[1][1]-line_points[0][1])*k*3]
                else:
                    vector = [(line_points[1][0]-line_points[0][0])*k, (line_points[1][1]-line_points[0][1])*k]

                if (line_points[0][0] > line_points[1][0] and line_points[0][1] < line_points[1][1]) or \
                        (line_points[0][0] < line_points[1][0] and line_points[0][1] > line_points[1][1]):
                    position = [vector[0]+line_points[0][0]-10, vector[1]+line_points[0][1]]
                elif line_points[0][0] == line_points[1][0]:
                    position = [vector[0]+line_points[0][0]-10, vector[1]+line_points[0][1]]
                elif line_points[0][1] == line_points[1][1]:
                    position = [vector[0]+line_points[0][0], vector[1]+line_points[0][1]-10]
                else:
                    position = [vector[0]+line_points[0][0], vector[1]+line_points[0][1]]
                list_distance_label.append(Label(canvas, text=str(data[i][j]), fg=label_fg_color, bg=label_bg_color))
                list_distance_label[len(list_distance_label)-1].place(x=position[0], y=position[1])
    return list_distance_label

def draw_best_distance(list_point, data, canvas, list_position, k):
    list_best_distance_label = []
    for i in range(1, len(list_point), 1):
        line_points = init_line_points(list_position[list_point[i-1]], list_position[list_point[i]])
        distance = math.sqrt((line_points[0][0]-line_points[1][0]) * (line_points[0][0]-line_points[1][0]) \
                   + (line_points[0][1]-line_points[1][1]) * (line_points[0][1]-line_points[1][1]))
        if distance < 300:
            vector = [(line_points[1][0]-line_points[0][0])*k*3, (line_points[1][1]-line_points[0][1])*k*3]
        else:
            vector = [(line_points[1][0]-line_points[0][0])*k, (line_points[1][1]-line_points[0][1])*k]

        if (line_points[0][0] > line_points[1][0] and line_points[0][1] < line_points[1][1]) or \
                (line_points[0][0] < line_points[1][0] and line_points[0][1] > line_points[1][1]):
            position = [vector[0]+line_points[0][0]-10, vector[1]+line_points[0][1]]
        elif line_points[0][0] == line_points[1][0]:
            position = [vector[0]+line_points[0][0]-10, vector[1]+line_points[0][1]]
        elif line_points[0][1] == line_points[1][1]:
            position = [vector[0]+line_points[0][0], vector[1]+line_points[0][1]-10]
        else:
            position = [vector[0]+line_points[0][0], vector[1]+line_points[0][1]]
        list_best_distance_label.append(Label(canvas, text=str(data[list_point[i-1]][list_point[i]]),
                                            fg=label_best_fg_color, bg=label_best_bg_color))
        list_best_distance_label[len(list_best_distance_label)-1].place(x=position[0], y=position[1])
    return list_best_distance_label

def draw_result(canvas, best_line, data):
    if best_line is not None:
        sum = 0
        text = 'Result: ' + str(best_line['path'][0]+1)
        for i in range(1, len(best_line['path']), 1):
            text = text + "->" + str(best_line['path'][i]+1) + "(" + \
                   str(data[best_line['path'][i-1]][best_line['path'][i]]) + ')'
            sum += data[best_line['path'][i-1]][best_line['path'][i]]
        text = text + " = " + str(sum)
        return text


