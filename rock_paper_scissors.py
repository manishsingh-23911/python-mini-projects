import random

print("Welcome to the game of rock, paper, scissors!")

def play_round():

    choice_1 = 'rock'
    choice_2 = 'paper'
    choice_3 = 'scissors'
    choice_4 = 'q'

    # Ask for the player's choice
    player_choice = input("Enter your choice rock/ paper/ scissors or enter 'q' to Quit: ").lower()


    # Validate input
    if player_choice not in [choice_1, choice_2, choice_3, choice_4]:
        print("Please enter a valid input")
        return False # returning False will indicate invalid input


    # If the user chooses 'q', end the game
    if player_choice == choice_4:
        print("Game Over. Goodbye!")
        return True # returning True will indicate game should end

    # Proceed with the game logic if the input is valid
    computers_choice = random.choice([choice_1, choice_2, choice_3])
    print(f"Computer's choice: {computers_choice}")

    # Determine the winner
    if player_choice == choice_1 and computers_choice == choice_2:
        print("Computer wins!")
    elif player_choice == choice_1 and computers_choice == choice_3:
        print("You win!")
    elif player_choice == choice_2 and computers_choice == choice_1:
        print("You win!")
    elif player_choice == choice_2 and computers_choice == choice_3:
        print("Computer wins!")
    elif player_choice == choice_3 and computers_choice == choice_1:
        print("Computer wins!")
    elif player_choice == choice_3 and computers_choice == choice_2:
        print("You win!")
    else:
        print("Game tied.")


    return False  # Continue the game after each round

# main loop to keep playing
while True:
    game_over = play_round()
    if game_over:
        break #Exit the loop if game is over or player chooses 'q'
    else:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again != 'y': # if player doesn't type 'y' stop playing
            print("Game over. Goodbye")
            break




