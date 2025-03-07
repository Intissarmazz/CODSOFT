print("_____Welcome to the game (Rock/Paper/Scissors) Made by Maaziz Intissar_____ ")
import random
name = input("Please enter your name or the player's name: ")
user_wins = 0
computer_wins = 0
tie = 0
while True:
    player_choice = input("Please enter your choice from this list: R(ock), S(cissors), P(aper) or Q(uit) the game: ").upper()
    if player_choice == "Q":
        print("You have exited the game")
    if player_choice != "R" and player_choice != "S" and player_choice != "P":
        continue
    if player_choice == "R":
        print("ROCK vs ", end=" ")
    elif player_choice == "P":
        print("PAPER vs ", end=" ")
    else:
        print("SCISSORS vs ", end=" ")
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computer_choice = "R"
        print("ROCK")
    elif randomNumber == 2:
        computer_choice = "P"
        print("PAPER")
    else:
        computer_choice = "S"
        print("SCISSORS")

    if player_choice == computer_choice:
        print("The match is a tie!")
        draws = tie + 1
        print(name, ":", user_wins, "tie:", draws, "PC:", computer_wins)
    elif player_choice == "R" and computer_choice == "P":
        print("You lost")
        computer_wins = computer_wins + 1
        print(name, ":", user_wins, "tie:", tie, "PC:", computer_wins)
    elif player_choice == "P" and computer_choice == "R":
        print("You won")
        user_wins = user_wins + 1
        print(name, ":", user_wins, "tie:", tie, "PC:", computer_wins)
    elif player_choice == "R" and computer_choice == "S":
        print("You won")
        user_wins = user_wins + 1
        print(name, ":", user_wins, "tie:", tie, "PC:", computer_wins)
    elif player_choice == "S" and computer_choice == "R":
        print("You lost")
        computer_wins = computer_wins + 1
        print(name, ":", user_wins, "tie:", tie, "PC:", computer_wins)
    elif player_choice == "S" and computer_choice == "P":
        print("You won")
        user_wins = user_wins + 1
        print(name, ":", user_wins, "tie:", tie, "PC:", computer_wins)
    elif player_choice == "P" and computer_choice == "S":
        print("You lost")
        computer_wins = computer_wins + 1
        print(name, ":", user_wins, "tie:", tie, "PC:", computer_wins)
    restart = input("Do you want to play again? (yes/no): ").strip().lower()
    if restart != "yes":
        print("Thanks for playing, see you soon!")
        break
















