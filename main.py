# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 02:27:57 2021

@author: ASUS
"""
from copy import deepcopy
from knn_test import get_digit_board
from sudoku_solver import print_board, solve
import pyautogui as pg
import numpy as np
import time

IMAGE_PATH = 'data/sudoku_screenshot.png'

#print(pg.position()) # check current cursor x-y position
WINDOW_X = 34 # x coordinate of top-left corner
WINDOW_Y = 262 # y coordinate of top-left corner
WINDOW_WIDTH = 566 # width of sudoku board
WINDOW_HEIGHT = 570 # height of sudoku board 

# screenshot sudoku window
im = pg.screenshot(region=(WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT))
im.save(IMAGE_PATH)

# auto-generate sudoku board
img_input, img_out, board_input = get_digit_board(IMAGE_PATH)
# cv2.imshow('im',img_input)
# cv2.imshow('out',img_out)
# cv2.waitKey(0)

# solve sudoku by back-tracking
board = deepcopy(board_input)
# determine whether the sudoku is solved or not 
finish_flag = False 
print("__________________________")
print_board(board)
print("__________________________")
print("")
print("- - - - - SOLVING - - - - -")
solve(board)
finish_flag = True
print("--------- FINISH ---------")

# print_board(board)

# simulate keyword actions
if finish_flag == True:
    print("Enjoy your game!!!")
    
    # mouse-click on digit on top-left corner to ready 
    for i in range(5,0,-1):
        print("Ready: ", i)
        time.sleep(1)
    
    # flatten the 2-D matrix into 1-D array
    board_array = np.reshape(board, (81))
    counter = 0
    
    for idx, num in enumerate(board_array):         
        pg.press(str(int(num)))
        pg.hotkey('right')
        counter = counter+1
         
        # go to next row after 9 inputs
        if counter == 9:
            pg.hotkey('down')
            for i in range(9):
                pg.hotkey('left')
            counter = 0

del board



    



