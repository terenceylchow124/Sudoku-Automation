# Sudoku Automation by KNN-OCR and Backtracking

In this project, we develop sudoku automation system to auto-solve sudoku puzzle from from [here](https://sudoku.com/medium/). First thing first, we grab the screen-shot image and track every positions of digits and manually labels every digits by using OpenCV. Then, we implement ***KNearest-Neighbors-Optical-Character-Recognizer (KNN-OCR)*** to detect and classify all sudoku digit. Now, the 9x9 sudoku board is ready in our programe. We apply ***Backtracking*** to solve the puzzle. Finally, we simulate keyboard actions by pyautogui 

Now, it's to time to play some games!!


# Training Steps
> - We normally need more than one screen-shot in order to train our KNN-OCR. So, take few screen-shot of sudoku and create "sudoku_train.png" manully by combining those. To skip this step, we provide you under data/.
> - For data collection, run digit_recongizer.py. The winodw will pop up, all you need to do is to input corresponding number. Two files will be saved under data/, they are "sudoku_data.data" and "sudoku_labels". Now, the training data and labels are all already.
> - Next, train KNN model as a digit recongizer by running knn_train.py. To skip this step, you can also use our trained model. 

# Testing Steps
> - Now, go to [sudoku.com](https://sudoku.com/medium/). And run main.py. 
> - The programe will automically take 4 steps: 
>   1. screenshot sudoku; 
>   2. recongize digit and generate sudoku board; 
>   3. solve by Backtracking;
>   4. simulate keyboard actions.
> - You may need to adjust WINDOW_X, WINDOW_Y, WINDOW_WIDTH and WINDOW_HEIGHT in main.py in order to take proper screenshot from your screen.  

# Acknowledgment
We refer reader to: 
1. [Python Sudoku Solver Tutorial with Backtracking](https://www.youtube.com/watch?v=eqUwSA0xI-s)
2. [Sudoku Automation](https://www.youtube.com/watch?v=jESGMTcrhSY)
3. [Optical Character Recognition (OCR) with KNN classifier](https://stackoverflow.com/questions/9413216/simple-digit-recognition-ocr-in-opencv-python)
