import random
import time

def check(comp, user):
    if comp == user:
        return 0
    
    if (comp == 0 and user == 1) or (comp == 1 and user == 2) or (comp == 2 and user == 0):
        return -1

    return 1

def play_game(num_of_games):
    user_wins = 0
    computer_wins = 0
    draws = 0

    for _ in range(num_of_games):
        comp = random.randint(0, 2)
        
        try:
            user = int(input("0 for Snake, 1 for Water, and 2 for Gun:\n"))
        except ValueError:
            print("Please enter a valid number (0, 1, or 2).")
            continue
        
        if user not in [0, 1, 2]:
            print("Please enter a correct value (0, 1, or 2).")
            continue

        score = check(comp, user)

        print("You:", user)
        print("Computer:", comp)

        if score == 0:
            print("It's a draw")
            draws += 1
        elif score == -1:
            print("You Lose")
            computer_wins += 1
        else:
            print("You Won")
            user_wins += 1

    print("\nSummary:")
    print("User Wins:", user_wins)
    print("Computer Wins:", computer_wins)
    print("Draws:", draws)

# Get user input for the number of times to play
try:
    num_of_games = int(input("Enter the number of times you want to play: "))
    play_game(num_of_games)
except ValueError:
    print("Please enter a valid number.")

time.sleep(2)  # Add a delay before exiting
