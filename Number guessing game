import random

def get_difficulty():
    while True:
        try:
            print("Choose difficulty level:")
            print("1. Easy (Number between 1 and 10)")
            print("2. Medium (Number between 1 and 50)")
            print("3. Hard (Custom range)")
            
            difficulty = int(input("Enter your choice (1, 2, or 3): "))
            if 1 <= difficulty <= 3:
                return difficulty
            else:
                print("Invalid input. Please choose a difficulty level between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_secret_number(difficulty):
    if difficulty == 1:
        return random.randint(1, 10)
    elif difficulty == 2:
        return random.randint(1, 50)
    elif difficulty == 3:
        while True:
            try:
                start_num = int(input("Enter the starting number: "))
                end_num = int(input("Enter the ending number: "))
                if start_num < end_num:
                    return random.randint(start_num, end_num)
                else:
                    print("Invalid input. Starting number should be less than the ending number.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")

def provide_feedback(secret_number, guess):
    difference = abs(secret_number - guess)
    if difference < 10:
        if secret_number > guess:
            print("A bit low. Try again.")
        else:
            print("A bit high. Try again.")
    elif guess < secret_number:
        print("Too low. Try again.")
    else:
        print("Too high. Try again.")

def play_game():
    print("Welcome to the Number Guessing Game!")
    player_name = input("Enter your name: ")
    
    score = 0
    while True:
        difficulty = get_difficulty()
        secret_number = generate_secret_number(difficulty)
        attempts = 0

        if difficulty == 1:
            print(f"\n{player_name}, you are playing on difficulty level {difficulty}. Guess the number between 1 and 10!")
        elif difficulty == 2:
            print(f"\n{player_name}, you are playing on difficulty level {difficulty}. Guess the number between 1 and 50!")
        else:
            print(f"\n{player_name}, you are playing on difficulty level {difficulty}. Enter a number between the specified range.")

        while True:
            try:
                guess = int(input("Your guess: "))
                attempts += 1

                if guess == secret_number:
                    print(f"Congratulations, {player_name}! You guessed the correct number in {attempts} attempts.")
                    score += 1
                    break
                else:
                    provide_feedback(secret_number, guess)
            except ValueError:
                print("Invalid input. Please enter a number.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print(f"\nThanks for playing, {player_name}! Your total score is {score}.")

if __name__ == "__main__":
    play_game()

