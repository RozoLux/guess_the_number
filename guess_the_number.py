import random

def guessTheNumber() :
    target_number = random.randint(1,100)
    attempts = 0

    while True :
        user_guess = int(input("Guess the number (1-100): "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Too low ! Try again.")
        else :
            print("Too high ! Try again.")

    if __name__ == "__main__":
        guessTheNumber()