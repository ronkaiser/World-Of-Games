from Live import load_game, welcome
from MemoryGame import play_memory
from GuessGame import play_guess
from CurrencyRouletteGame import play_currency
from Score import add_score
from MainScores import score_serve, app
import Utils

Utils.reset_score()
Utils.clear_screen()
user_name = input("please enter your name:\n")
Utils.clear_screen()
print(welcome(user_name))

def play_game(chosen_game, difficulty):
    if chosen_game == 1:
        Utils.clear_screen()
        win = play_memory(difficulty)
        if win:
            add_score(difficulty)
    if chosen_game == 2:
        Utils.clear_screen()
        win = play_guess(difficulty)
        if win:
            add_score(difficulty)
    if chosen_game == 3:
        Utils.clear_screen()
        win = play_currency(difficulty)
        if win:
            add_score(difficulty)

chosen_game, difficulty = load_game()
play_game(int(chosen_game), int(difficulty))
score_serve()