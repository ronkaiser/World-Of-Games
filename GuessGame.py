import random

def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    guessed_number = input(f"Please guess number between 1 to {difficulty} \n")
    while not guessed_number.isdigit():
        print("Wrong input, please enter digits")
        guessed_number = input(f"Please guess number between 1 to {difficulty} \n")
    guessed_number = int(guessed_number)
    return guessed_number

def compare_results(secret_number, guessed_number):
    if secret_number == guessed_number:
        print(f"You WON! the number was {secret_number}")
        return True
    else:
        print(f"You LOSE, the number was {secret_number}")
        return False

def play_guess(difficulty):
    secret_number = generate_number(difficulty)
    guessed_number = get_guess_from_user(difficulty)
    return compare_results(secret_number, guessed_number)