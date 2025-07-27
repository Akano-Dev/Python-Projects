import random

option = ["rock", "paper", "scissors"]

while True:

    user_choice = input("Enter rock, paper, or scissors : ").lower()

    if user_choice not in option:
        print("Invalid Option! Please try again")
        continue

    computer_choice = random.choice(option)
    print(f"Computer Choose {computer_choice}")

    if user_choice == computer_choice:
        print("IT'S DRAW!")
    elif (user_choice == "rock" and computer_choice == "scissors")or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "rock"):
        print("YOU WIN!😍")
    else:
        print("YOU LOSE!😂")

    again=input("Wanna play again? [Yes/No] : ").lower()
    if again != "Yes":                              #There's some error in error I guess . Gonna fix it later!
        print("Thanks for playing")
        break