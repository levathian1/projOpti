import pandas as pd
import numpy as np
import random
import pygame
import time
import copy

matrix = pd.read_csv("freqBigrammes.txt", sep = "\t", header=0, index_col=0)

key_array = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

perm_key_arr = np.array([["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o", "p", "q", "r", "s", "t"], ["u", "v", "w", "x", "y", "z", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]])

perm_key = list("abcdefghijklmnopqrstuvwxyz")

current_layout = key_array

tabul = list()
tabu = 10
max_iter = 50

def get_bigram_val(x, y):
    #print("val ", matrix.loc[x][y])
    return int(matrix.loc[x][y])

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
                big = get_bigram_val(key, next)
                dist = dist * get_bigram_val(key, next)
                #print("big: ", dist, big)
    
    return dist


def distance_manhattan(key1, key2):
    return abs(key1[0]-key2[0])+abs(key1[1]-key2[1])

def obj(kb):
    res = 0
    for i in range(0, 4):
        for j in range(0, 9):
            if(kb[i][j] != " " and kb[i][j+1] != " "):
                key = kb[i, j]
                key = key.upper() + "_"
                next = kb[i, j+1]
                next ="_" + next.upper()
                key1 = (j, i)
                key2 = (j+1, i)
               #print(distance_manhattan(key1, key2))
                res = res + get_bigram_val(key, next) * distance_manhattan(key1, key2)
                #print("res : ", res)
    return res

def distance_manhattan_on_kb(kb):
    distance = 0
    for i in range (0, 4):
        for j in range(0, 9):
            key1 = (j, i)
            key2 = (j+1, i)
            #print(row, col, letter, np.where(kb == letter)[0])
            distance = distance + distance_manhattan(key1, key2)
    #print("here ", distance)
    return distance

best_kb = current_layout
best_d = obj(best_kb)

def swap_keys(kb):
    new_layout = copy.copy(kb)
    iy, jy = random.sample(range(10), 2) 
    ix, jx = random.sample(range(4), 2) 
    old = (new_layout[ix][iy], new_layout[jx][jy])
    new_layout[ix][iy], new_layout[jx][jy] = new_layout[jx][jy], new_layout[ix][iy]
    return new_layout, old



pygame.init()

bg_color = (255, 255, 255)
cell_color = (0, 0, 0)

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Keyboard Layout Configuration")

font = pygame.font.Font('freesansbold.ttf', 15)

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
    new_layout, old = swap_keys(best_kb)
    print(old)
    if (tabul.count(old) == 0):
        new_distance = obj(new_layout)
        print(new_distance, best_d)
        if new_distance < best_d:
            current_layout = new_layout
            best_d = new_distance
            best_kb = new_layout
            tabul.append(old)
            print("better")
            print(best_kb)
        else:
            print("not better")
            print(best_kb)
    nb = "iterations: " + str(i)
    pair = "considered pair: " + str(old[0]) + " " +str(old[1])
    distance_t = "best distance: " + str(best_d) + " current swap distance: " + str(new_distance)
    print(new_distance, best_d)
    draw_matrix(best_kb)
    text2 = font.render(nb, True, (255, 255,255), (0, 0, 0))
    text3 = font.render(pair, True, (255, 255,255), (0, 0, 0))
    text4 = font.render(distance_t, True, (255, 255,255), (0, 0, 0))
    screen.blit(text2, (200, 300))
    screen.blit(text3, (200, 400))
    screen.blit(text4, (000, 500))
    pygame.display.update()
    

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