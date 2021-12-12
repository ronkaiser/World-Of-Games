from forex_python.converter import CurrencyRates
import random


def get_money_interval(difficulty):
    curr = CurrencyRates()
    t = random.randint(1, 100)
    total = curr.get_rate('USD', 'ILS') * t
    low = total-(5-difficulty)
    high = total + (5-difficulty)
    print(f"Please guess how much is {t} USD in ILS?")
    return low, high


def get_guess_from_user():
    user_guess = input("Your guess is: ")
    while not user_guess.isdigit():
        print("Wrong input, please enter digits")
        user_guess = input("Your guess is: ")
    user_guess = float(user_guess)
    return user_guess

def play_currency(difficulty):
    low, high = get_money_interval(difficulty)
    user_guess = get_guess_from_user()
    if low <user_guess < high:
        print("You Won!")
        print(f"Range of guess was between {low} and {high} and your guess was {user_guess}")

    else:
        print("You Lose")
        print(f"Range of guess was between {low} and {high} and your guess was {user_guess}")