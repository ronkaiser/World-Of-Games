import os, Utils

scorefile = Utils.SCORES_FILE_NAME

def add_score(difficulty):
    if not os.path.exists('./Scores.txt'):
        Utils.reset_score()
    with open(scorefile, 'r') as readfile:
        current_score = readfile.read()
        POINTS_OF_WINNING = (difficulty * 3) + 5
        new_score = int(current_score) + POINTS_OF_WINNING
        new_score = str(new_score)
        with open(scorefile, 'w') as writefile:
            writefile.writelines(new_score)
            writefile.close()
    readfile.close()