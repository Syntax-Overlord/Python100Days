art = r"""
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
"""


def Number() -> int:
    import random

    return random.randint(1, 100)


def check_guess(guess: int, number: int) -> str:
    if guess < number:
        return "Too low!"
    elif guess > number:
        return "Too high!"
    else:
        return "Correct!"


def difficulty_level() -> int:
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return 10
    else:
        return 5


def play_game():
    print(art)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = Number()
    attempts = difficulty_level()
    for _ in range(attempts):
        guess = int(input("Make a guess: "))
        result = check_guess(guess, number)
        if result == "Correct!":
            break
        else:
            print(result)
    else:
        print(f"You've run out of attempts. The number was {number}.")
