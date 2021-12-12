import random, time, Utils

def generate_sequence(difficulty):
    random_numbers = [random.randrange(1, 101)for n in range(difficulty)]
    print(random_numbers)
    time.sleep(0.7)
    Utils.clear_screen()
    return random_numbers

def get_list_from_user(difficulty):
    guessed_numbers = []
    print("Try to guess the numbers ")
    for n in range(difficulty):
        input_from_user = input("Enter number: ")
        while not input_from_user.isdigit():
            print("Wrong input, please enter digits")
            input_from_user = input("Enter number: ")
        guessed_numbers.append(int(input_from_user))
    return guessed_numbers

def is_list_equal(random_numbers, guessed_numbers):
    if sorted(random_numbers) == sorted(guessed_numbers):
        print(f"You Won! the numbers was: {random_numbers}")
        return True
    else:
        print(f"You LOSE! the numbers was: {random_numbers}")
        return False

def play_memory(difficulty):
    random_numbers = generate_sequence(difficulty)
    guessed_numbers = get_list_from_user(difficulty)
    return is_list_equal(random_numbers, guessed_numbers)