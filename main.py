import pandas as pd
import random

matrix = pd.read_csv("freqBigrammes.txt", sep = "\t")

keys = list("abcdefghijklmnopqrstuvwxyz")
perm_key = list("abcdefghijklmnopqrstuvwxyz")

current_layout = keys

tabul = list()
tabu = 10
max_iter = 100

def distance_manhattan(p1x, p1y, p2x, p2y):
    return abs(p1x-p2x)+abs(p1y-p2y)

def distance_manhattan_on_kb(kb, perm=perm_key):
    distance = 0
    lrow, lcol = 0, 0
    for letter in perm_key:
        row, col = kb.index(letter)//10, kb.index(letter)%10
        distance = distance_manhattan(row, lrow, col, lcol)
        lrow, lcol = row, col
    return distance

def swap_keys(kb):
    new_layout = kb
    i, j = random.sample(range(len(kb)), 2)
    new_layout[i], new_layout[j] = new_layout[j], new_layout[i]
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
print(best_kb)