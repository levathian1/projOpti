import pandas as pd
import numpy as np
import random
import pygame
import time

matrix = pd.read_csv("freqBigrammes.txt", sep = "\t", header=0, index_col=0)

key_array = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

perm_key_arr = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

perm_key = list("abcdefghijklmnopqrstuvwxyz")

current_layout = key_array
current_pair = list()

tabul = list()
tabu = 10
max_iter = 50

def get_bigram_val(x, y):
    return matrix.loc[x][y]

def current_matrix():
    return current_layout

def get_kb_bigram(kb, dist):
    for i in range(0, 4):
        for j in range(0, 9):
            if(kb[i][j] != " " and kb[i][j+1] != " "):
                key = kb[i, j]
                key = key.upper() + "_"
                next = kb[i, j+1]
                next ="_" + next.upper()
                dist = dist * get_bigram_val(key, next)
    return dist


def distance_manhattan(key1, key2):
    return abs(key1[0]-key2[0])+abs(key1[1]-key2[1])

def distance_manhattan_on_kb(kb):
    distance = 0
    for i in range (0, 4):
        for j in range(0, 9):
            key1 = (j, i)
            key2 = (j+1, i)
            #print(row, col, letter, np.where(kb == letter)[0])
            distance = distance + distance_manhattan(key1, key2)
    return distance

def swap_keys(kb):
    new_layout = kb
    iy, jy = random.sample(range(10), 2) 
    ix, jx = random.sample(range(4), 2) 
    new_layout[ix][iy], new_layout[jx][jy] = new_layout[jx][jy], new_layout[ix][iy]
    return new_layout

best_kb = current_layout
best_d = get_kb_bigram(best_kb, distance_manhattan_on_kb(best_kb))

pygame.init()

bg_color = (255, 255, 255)
cell_color = (0, 0, 0)

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Keyboard Layout Configuration")

font = pygame.font.Font('freesansbold.ttf', 30)

def draw_matrix(matrix_data):
    # Clear the screen
    screen.fill(bg_color)

    # Draw each cell in the matrix
    for y in range(4):
        for x in range(10):
            # Calculate the position of the cell on the screen
            rect = pygame.Rect(x * 50, y * 50, 50, 50)
            # Draw the cell
            pygame.draw.rect(screen, cell_color, rect, 1)
            # Draw the text in the cell
            text = font.render(current_layout[y][x], True, cell_color)
            text_rect = text.get_rect(center=rect.center)
            screen.blit(text, text_rect)
    

    # Update the display
    pygame.display.flip()



for i in range (0, max_iter):
    new_layout = swap_keys(current_layout)
    if new_layout not in tabul:
        new_distance = get_kb_bigram(best_kb, distance_manhattan_on_kb(best_kb))
        if new_distance < best_d:
            current_layout = new_layout
            best_d = new_distance
            best_kb = new_layout
            tabul.append(new_layout)
    nb = "iterations: " + str(i)
    draw_matrix(current_layout)
    text2 = font.render(nb, True, (255, 255,255), (0, 0, 0))
    screen.blit(text2, (200, 300))
    pygame.display.update()
    print(current_layout)

    time.sleep(1)

# Draw the initial state of the matrix

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
   




#print(matrix)
print(perm_key)
print("original layout")
print(perm_key_arr)
print("new layout")
print(best_kb)