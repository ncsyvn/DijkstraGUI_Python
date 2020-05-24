# DijkstraGUI_Python
Problem: Find the best distance (min distance) from 2 point base on Dijkstra algorithm?
Solve:
  1. Input amount of point user want to init and amount of relationship (line) which connect two point
     Program auto generate data after input and can generate many time after click button submit.
  2. Base on data which are inited, tab show data by graph.
     When user choose 2 point to find best distance:
        if haven't distance:
            Show message warning
        else:
            Show result: result will be paint by difference color (result base on dijkstra algorithm)
     User can choose difference 2 point to find another result.
Tech:
    1. Python language
    2. Tkinter library to graph
