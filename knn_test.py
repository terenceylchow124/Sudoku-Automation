# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 03:28:05 2021

@author: ASUS
"""
import cv2
import numpy as np

WIDTH = 64
HEIGHT = 64
TOPLEFT_X = 31
TOPLEFT_Y = 42
CENTER_POSITION_X = np.zeros((1,9))
CENTER_POSITION_Y = np.zeros((9,1))
board = np.zeros((9,9), dtype=np.int8)

def get_digit_board(IMAGE_PATH, MODEL_PATH="sudoku_digit_model.xml"):
    
    # load trained KNN model
    model = cv2.ml.KNearest_load(MODEL_PATH)
    
    # load sudoku screenshot
    im = cv2.imread(IMAGE_PATH)
    out = np.zeros(im.shape,np.uint8)
    
    # image preprocess
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray,255,1,1,11,2)
    
    # capture all possible digits positions from image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    # define all digit centers from image
    for i in range(9):
        CENTER_POSITION_X[0,i] = TOPLEFT_X+i*WIDTH
        CENTER_POSITION_Y[i,0] = TOPLEFT_Y+i*HEIGHT
        # cv2.circle(im, (TOPLEFT_X+i*WIDTH,TOPLEFT_Y+j*HEIGHT), radius=1, color=(0, 0, 255), thickness=1)
     
    # iterate over all possible squares
    for cnt in contours:
        if cv2.contourArea(cnt)>50:
            [x,y,w,h] = cv2.boundingRect(cnt)
            digit_center_x = int(x+w/2)
            digit_center_y = int(y+h/2)
            
            # filter by square height conditions
            if  h>28 and h < 50:
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
                
                # region of interest
                roi = thresh[y:y+h,x:x+w]
                
                # preprocess region of interest
                roismall = cv2.resize(roi,(10,10))
                roismall = roismall.reshape((1,100))
                roismall = np.float32(roismall)
                
                # classify digit by KNN model
                retval, results, neigh_resp, dists = model.findNearest(roismall, k = 5)
                
                # draw digit tag on output window
                string = str(int((results[0][0])))
                cv2.putText(out,string,(x,y+h),0,1,(0,255,0))
                
                # locate digits into 9x9 board
                diff_x = abs(CENTER_POSITION_X - digit_center_x)
                diff_y = abs(CENTER_POSITION_Y - digit_center_y)
                board[np.argmin(diff_y), np.argmin(diff_x)] = int((results[0][0]))
    
    return im, out, board

if __name__ == "__main__":
    IMAGE_PATH = 'data/sudoku_test.png'
    im, out, board = get_digit_board(IMAGE_PATH)
    print("digit recongizer test complete")
    cv2.imshow('input',im)
    cv2.imshow('output',out)
    cv2.waitKey(0)
