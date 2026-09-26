import random
import time

choices = ["ROCK", "PAPER", "SCISSORS"]     # this are the choices
player_points = 0                           # player's point
computer_points = 0                         # computer's point
player_name = input("Enter your name: ")    # and the player"s name since why not

playing = True

while playing:
    print("\nChoose between [ ROCK | PAPER | SCISSORS ] or [Q to quit]")
    user_choice = input("Type here ---> ").upper()
    
    if user_choice == "Q":              # if the user press "q" the game will stop
        playing = False
        continue

    if user_choice not in choices:      # if the user pick other than the 4 choices they have it wil loop back from the beginning
        print("\nChoose only the available listed choices you have")
        time.sleep(1)
        continue

    computer_choice = random.choice(choices)

    print(f"\n{player_name} choice: [{user_choice}]")   # this will display the player and computer choice
    print(f"Computer choice: [{computer_choice}]\n")

    # this will check who ever win or lose AND add points to the winner
    if user_choice == computer_choice:
        print("Its a tie")
    elif user_choice == "ROCK" and computer_choice == "SCISSORS":
        print("You win!")
        player_points += 1
    elif user_choice == "PAPER" and computer_choice == "ROCK":
        print("You win!")
        player_points += 1
    elif user_choice == "SCISSORS" and computer_choice == "PAPER":
        print("You win!")
        player_points += 1
    else:
        print("You lose!")
        computer_points += 1

    # this will show the current point status
    print("[Points Status]")
    print(f"{player_name} pts ({player_points}) | Computer pts ({computer_points})")

    # ask if the player would like to play again or not
    while True:
        retry = input("\nPlay again? y/N: ").upper()

        if retry not in ["Y", "N"]:
            continue
        else:
            if retry == "Y":
                break
            elif retry == "N": 
                playing = False
                break

print(f"\nThanks for playing {player_name} goodbye")
