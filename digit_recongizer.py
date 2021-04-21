# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 03:17:05 2021

@author: ASUS
"""
import numpy as np
import cv2

cv2.namedWindow("norm", cv2.WINDOW_NORMAL) 

def data_collection(IMAGE_PATH):
    
    # load image 
    im = cv2.imread(IMAGE_PATH)
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    
    # image preprocess
    blur = cv2.GaussianBlur(gray,(5,5),0)
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    
    # capture all possible digits positions from image
    contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    
    data =  np.empty((0,100))
    labels = []
    keys = [i for i in range(48,58)]
    early_stop = False
       
    # iterate over all possible squares
    for cnt in contours:
        if cv2.contourArea(cnt)>50:
            [x,y,w,h] = cv2.boundingRect(cnt)
            
            # filter by square height conditions
            if  h>28 and h < 50:
                target = im[y:y+h,x:x+w]
                
                # draw rectangle on region of interest
                cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
                
                # region of interest
                roi = thresh[y:y+h,x:x+w]
                roismall = cv2.resize(roi,(10,10))
                
                # find centers of current roi
                center = (int(y+h/2), int(x+w/2))
                print(center)
                
                cv2.imshow('norm',im) 
                key = cv2.waitKey(0)
                
                # input either "ESC" to terminal or corresponding digit
                if key == 27:  # (escape to quit)
                    cv2.destroyAllWindows()
                    early_stop = True
                    break
                elif key in keys:
                    labels.append(int(chr(key)))
                    sample = roismall.reshape((1,100))
                    data = np.append(data,sample,0)
                cv2.rectangle(im,(x,y),(x+w,y+h),(255,0,0),2)
    
    if early_stop == False:
        cv2.imshow('norm',im)     
        
        # any keys to close window
        if cv2.waitKey(0): 
            cv2.destroyAllWindows()             
    return data, labels

if __name__ == "__main__":      
    IMAGE_PATH = 'data/sudoku_train.png'
    data, labels = data_collection(IMAGE_PATH)
    labels = np.array(labels,np.float32)
    labels = labels.reshape((labels.size,1))
    print("data collection complete")
    
    np.savetxt('data/sudoku_data.data',data)
    np.savetxt('data/sudoku_labels.data',labels)
