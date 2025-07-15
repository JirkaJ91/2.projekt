"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Jiří Jetmar
email: jetm.jirka@gmail.com
"""

import random
import time 


game_statistics = []

def generate_secret_number():
    
    digits = list("0123456789")
    random.shuffle(digits)

    if digits[0] == '0':
        non_zero_indices = [i for i, d in enumerate(digits) if d != '0']
        if non_zero_indices:
            swap_index = random.choice([idx for idx in non_zero_indices if idx != 0])
            digits[0], digits[swap_index] = digits[swap_index], digits[0]

    secret = "".join(digits[:4])
    return secret
print()
def get_feedback(secret, guess):
    
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return bulls, cows

def validate_guess(guess):
    
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

def format_plural(count, word_singular, word_plural):
    
    if count == 1:
        return f"{count} {word_singular}"
    return f"{count} {word_plural}"

def play_game():
    
    secret_number = generate_secret_number()
    attempts = 0
    
    
    start_time = time.time()

    separator_length = 35
    print("Hi there!")
    print("-" * separator_length)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * separator_length)

    while True:
        attempts += 1
        print("-" * separator_length) 
        guess = input(f"Enter a number: ")

        if not validate_guess(guess):
            continue

        bulls, cows = get_feedback(secret_number, guess)

        if bulls == 4:
           
            end_time = time.time()
            game_duration = round(end_time - start_time, 2)

            print("-" * separator_length)
            print(f"Correct, you've guessed the right number in {attempts} {'attempt' if attempts == 1 else 'attempts'}!")
            print(f"It took you {game_duration} seconds.")
            print("-" * separator_length)
            
            
            game_statistics.append((attempts, game_duration))
            break
        else:
            bulls_str = format_plural(bulls, "bull", "bulls")
            cows_str = format_plural(cows, "cow", "cows")
            print(f"{bulls_str}, {cows_str}")

def display_statistics():
    
    if not game_statistics:
        print("\n--- No games played to display statistics. ---")
        return

    print("\n--- Game statistics ---")
    for i, (attempts, duration) in enumerate(game_statistics):
        print(f"Game {i+1}: Attempts: {attempts}, Time: {duration} seconds")
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
    while True:
        play_game()
        display_statistics()
        
        
        play_again = input("Do you to want play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break