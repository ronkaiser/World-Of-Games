import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = "500"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_score():
    scorefile = SCORES_FILE_NAME
    with open(scorefile, 'w') as writefile:
        writefile.writelines('0')
        writefile.close()