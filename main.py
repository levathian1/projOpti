import pandas as pd
import numpy as np
import random

matrix = pd.read_csv("freqBigrammes.txt", sep = "\t")

key_array = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

perm_key_arr = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

perm_key = list("abcdefghijklmnopqrstuvwxyz")

current_layout = key_array
current_pair = list()

tabul = list()
tabu = 10
max_iter = 5

def get_bigram_val(x, y):
    return matrix.loc[x][y]

def distance_manhattan(p1x, p1y, p2x, p2y):
    return abs(p1x-p2x)+abs(p1y-p2y)

def distance_manhattan_on_kb(kb, perm=perm_key):
    distance = 0
    lrow, lcol = 0, 0
    for letter in perm_key:
        row, col = np.where(kb == letter)[0], np.where(kb == letter)[1]
        print(row, col, letter, np.where(kb == letter)[0])
        distance = distance + distance_manhattan(row, lrow, col, lcol)
        lrow, lcol = row, col
    return distance

def swap_keys(kb):
    new_layout = kb
    ix, iy,  jx, jy = random.sample(range(len(kb)), 4)
    new_layout[ix][iy], new_layout[jx][jy] = new_layout[jx][jy], new_layout[ix][iy]
    return new_layout

best_kb = current_layout
best_d = distance_manhattan_on_kb(best_kb)

for i in range (0, max_iter):
    new_layout = swap_keys(current_layout)
    if tuple(new_layout) not in tabul:
        new_distance = distance_manhattan_on_kb(new_layout)
        if new_distance < best_d:
            current_layout = new_layout
            best_d = new_distance
            best_kb = new_layout
            tabul.append(new_layout)


#print(matrix)
print(perm_key)
print(perm_key_arr)
print(best_kb)