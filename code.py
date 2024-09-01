import random

def generate_code(length=4):
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Red, Green, Blue, Yellow, Orange, Purple
    return random.sample(colors, length)

def get_feedback(secret_code, guess):
    correct_position = sum(s == g for s, g in zip(secret_code, guess))
    correct_color = sum(min(secret_code.count(c), guess.count(c)) for c in set(guess))
    return correct_position, correct_color - correct_position

def play_game():
    secret_code = generate_code()
    attempts = 10
    print("Welcome to Mastermind!")
    print(f"Guess the {len(secret_code)}-color code. You have {attempts} attempts.")

    while attempts > 0:
        guess = input("Enter your guess: ").upper().split()
        if len(guess) != len(secret_code):
            print(f"Please enter exactly {len(secret_code)} colors.")
            continue

        correct_position, correct_color = get_feedback(secret_code, guess)
        print(f"Correct positions: {correct_position}, Correct colors: {correct_color}")

        if correct_position == len(secret_code):
            print("Congratulations! You guessed the code.")
            break

        attempts -= 1

    if attempts == 0:
        print(f"Game over! The correct code was {secret_code}")

if __name__ == "__main__":
    play_game()
