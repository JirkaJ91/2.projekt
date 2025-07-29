"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Jetmar
email: jetm.jirka@gmail.com
"""

import random
import time
from typing import List, Tuple


game_statistics: List[Tuple[int, float]] = []


def generate_secret_number() -> str: #Generuje náhodné čtyřmístné číslo s unikátními číslicemi, které nezačíná nulou.
    
    first_digit = str(random.randint(1, 9))

    remaining_digits = list("0123456789")

    remaining_digits.remove(first_digit)  

    random.shuffle(remaining_digits)

    secret = first_digit + "".join(remaining_digits[:3])
    return secret


def get_feedback(secret: str, guess: str) -> Tuple[int, int]: #Poskytuje zpětnou vazbu k hádání, udávající počet "bulls" a "cows".
    
    bulls = 0
   
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows


def validate_guess(guess: str) -> bool: #Validuje uživatelský vstup pro hádání.
    
    if not guess.isdigit():
        print("Invalid input! The guess must contain only digits.")
        return False
    if len(guess) != 4:
        print("Invalid input! The guess must be exactly a four-digit number.")
        return False
    if len(set(guess)) != 4:
        print("Invalid input! Digits in the guess must not repeat.")
        return False
    if guess[0] == '0':
        print("Invalid input! The guess must not start with zero.")
        return False
    return True


def format_plural(count: int, word_singular: str, word_plural: str) -> str: #Vrátí správný tvar slova (jednotné/množné číslo) na základě počtu.
    
    if count == 1:
        return f"{count} {word_singular}"
    return f"{count} {word_plural}"


def play_game() -> bool: #Hlavní funkce pro hraní hry Bulls and Cows.
    
    secret_number = generate_secret_number()
    attempts = 0

    start_time = time.time()

    separator_length = 35
    print("Hi there!")
    print("-" * separator_length)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * separator_length)

    try:
        while True:
            attempts += 1
            print("-" * separator_length)
            guess = input("Enter a number: ").strip()  

            if not validate_guess(guess):
                continue

            bulls, cows = get_feedback(secret_number, guess)

            if bulls == 4:
                end_time = time.time()
                game_duration = round(end_time - start_time, 2)

                print("-" * separator_length)
                print(f"Correct, you've guessed the right number in {attempts} "
                      f"{'attempt' if attempts == 1 else 'attempts'}!")
                print(f"It took you {game_duration} seconds.")
                print("-" * separator_length)

                game_statistics.append((attempts, game_duration))
                break
            else:
                bulls_str = format_plural(bulls, "bull", "bulls")
                cows_str = format_plural(cows, "cow", "cows")
                print(f"{bulls_str}, {cows_str}")
    except EOFError: 
        print("\nInput interrupted. Exiting game.")
        return False  
    except KeyboardInterrupt: 
        print("\nGame interrupted by user. Exiting.")
        return False  
    except Exception as e: 
        print(f"\nAn unexpected error occurred during the game: {e}")
        return False  
    return True  


def display_statistics() -> None: #Zobrazuje statistiky odehraných her.

    if not game_statistics:
        print("\n--- No games played to display statistics. ---")
        return

    print("\n--- Game statistics ---")
    for i, (attempts, duration) in enumerate(game_statistics):
        print(f"Game {i + 1}: Attempts: {attempts}, Time: {duration} seconds")
    print("-" * 30)

    if game_statistics:
        total_attempts = sum(s[0] for s in game_statistics)
        total_duration = sum(s[1] for s in game_statistics)

        avg_attempts = total_attempts / len(game_statistics)
        avg_duration = total_duration / len(game_statistics)

        print(f"Average number of attempts: {avg_attempts:.2f}")
        print(f"Average game time: {avg_duration:.2f} seconds")
        print("-" * 30)


if __name__ == "__main__":
    try:
        while True:
            if not play_game():  
                break
            display_statistics()

        
            try:
                play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            except (EOFError, KeyboardInterrupt):
                print("\nInput interrupted. Thanks for playing! Goodbye.")
                break  

            if play_again != 'yes':
                print("Thanks for playing! Goodbye.")
                break
    except Exception as e:
        print(f"\nAn unrecoverable error occurred: {e}")
        print("The program has terminated unexpectedly.")