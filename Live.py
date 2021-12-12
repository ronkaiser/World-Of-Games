import Utils

def welcome(user_name):
    welcome_message = f"Hello {user_name} and welcome to the World of Games (WoG).\n" \
                      f"Here you can find many cool games to play."
    return welcome_message


def load_game():
    chosen_game = None
    while chosen_game not in range(1, 4):
        Utils.clear_screen()
        chosen_game = input("Please choose a game to play:\n"
                               "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it"
                               " back\n"
                               "2. Guess Game - guess a number and see if you chose like the computer\n"
                               "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n")
        if chosen_game.isdigit():
           chosen_game = int(chosen_game)

    difficulty = None
    while difficulty not in range(1, 6):
        Utils.clear_screen()
        difficulty = input("Please choose difficult from 1 to 5\n")
        if difficulty.isdigit():
           difficulty = int(difficulty)

    return chosen_game, difficulty