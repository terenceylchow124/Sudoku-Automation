# sudoku_automating 
Automating sudoku by back-tracking 

In this project, we apply back-tracking technique to [solve the sudoku](https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/). We generate sudoku board by automically grab the screen-shot image from [here](https://sudoku.com/medium/). We track every positions of digits and manually labels every digits by using OpenCV libaray. The machine learning model, KNN, is trained to classify all digits. We save the trained model in .xml formatting. 

Now, it's to automating sudoku. 

# Training Steps
> - Take few screen-shot of sudoku and create you "sudoku_train.png" manully by combining those. You can also use ours, so you can skip this skip. 
> - Data collection. Run digit_recongizer.py. The winodw will pop up, all you need to do is to input corresponding number. Two .data files will be saved under data/, they are "sudoku_data.data" and "sudoku_labels". Now, the training data and labels are all already.
> - Next, train KNN model as a digit recongizer by running knn_train.py. To skip this step, you can also use our trained model. 


# Testing Steps
> - Now, you're good to go. Go to [sudoku.com](https://sudoku.com/medium/). And run main.py. 
> - The programe will automically take 4 steps: 1) screenshot sudoku; 2) recongize digit and generate sudoku board; 3) solve by back-tracking, 4) simulate keyboard actions.
> - Note that, you may need to adjust WINDOW_X, WINDOW_Y, WINDOW_WIDTH and WINDOW_HEIGHT in main.py in order to take proper screenshot. 
