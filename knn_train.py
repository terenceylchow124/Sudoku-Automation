# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 03:23:54 2021

@author: ASUS
"""

import cv2
import numpy as np

def model_train(SUDOKU_TRAIN_DATA_PATH, SUDOKU_TRAIN_LABEL_PATH, MODEL_PATH):
    
    # load training data and label
    samples = np.loadtxt(SUDOKU_TRAIN_DATA_PATH, np.float32)
    responses = np.loadtxt(SUDOKU_TRAIN_LABEL_PATH, np.float32)
    responses = responses.reshape((responses.size,1))
    
    # define and train knn model
    model = cv2.ml.KNearest_create()
    model.train(samples,cv2.ml.ROW_SAMPLE,responses)
    model.save(MODEL_PATH)
    
if __name__=="__main__":
    MODEL_PATH = 'sudoku_digit_model.xml'
    SUDOKU_TRAIN_DATA_PATH = 'data/sudoku_data.data'
    SUDOKU_TRAIN_LABEL_PATH = 'data/sudoku_labels.data'
    
    model_train(SUDOKU_TRAIN_DATA_PATH, SUDOKU_TRAIN_LABEL_PATH, MODEL_PATH)
    print("digit recongizer training complete")