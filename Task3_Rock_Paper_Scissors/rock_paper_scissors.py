import random

choices = ["rock", "paper", "scissors"]

while True:

    user = input("\nEnter Rock, Paper or Scissors: ").lower()

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if user == computer:
        print("It's a Tie!")

    elif user == "rock" and computer == "scissors":
        print("You Win!")

    elif user == "paper" and computer == "rock":
        print("You Win!")

    elif user == "scissors" and computer == "paper":
        print("You Win!")

    elif user in choices:
        print("Computer Wins!")

    else:
        print("Invalid Choice!")

    play_again = input("Play Again? (yes/no): ").lower()

    if play_again != "yes":
        print("Game Over!")
        break
