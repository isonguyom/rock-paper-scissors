# Rock-Paper-Scissors game
# Create a list to store the three options R = Rock, P = Paper, S = Scissors
import random

game_is_running = True
print("Welcome to Rock-Paper-Scissors game. ENJOY...")
while game_is_running:

    option_list = ["R", "P", "S"]

    # Request player option from (R, P, S)
    player = input("Player(What is your choice: R, P, S): ")
    # Convert player option to upper case
    player_upper = player.upper()
    
    # Check player's choice validity
    if player_upper in option_list:
        # Change player option letter to the word it represents
        global player_choice
        if player_upper == "R":   
            player_choice = "Rock"
        if player_upper == "P":
            player_choice = "Paper"
        if player_upper == "S":
            player_choice = "Scissors"

        # Generator random computer option from option_list
        computer = random.choice(option_list)
        # Change computer choice letter to the word it represents
        global computer_choice
        if computer == "R":   
            computer_choice = "Rock"
        if computer == "P":
            computer_choice = "Paper"
        if computer == "S":
            computer_choice = "Scissors"
        
        # Print output
        print("Player (", player_choice, ") : CPU (", computer_choice, ")")
        
        # Determine winner, loser, or draw
        if player_choice == computer_choice:
            print(f"You both selected {player_choice}. IT'S A TIE!")
            continue
        elif player_choice == "Rock":
            if computer_choice == "Scissors":
                print("Rock crushes scissors! YOU WIN!")
            else:
                print("Paper covers rock! YOU LOSE.")
        elif player_choice == "Paper":
            if computer_choice == "Rock":
                print("Paper covers rock! YOU WIN!")
            else:
                print("Scissors cuts paper! YOU LOSE.")
        elif player_choice == "Scissors":
            if computer_choice == "Paper":
                print("Scissors cuts paper! YOU WIN!")
            else:
                print("Rock crushes scissors! YOU LOSE.")
        
    else:
        # If player choice is not valid
        print("Invalid selection")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            break

    game_is_running = False
