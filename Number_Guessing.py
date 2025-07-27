import random

secret_number =  random.randint(1,100)

tries = 0

while True:
    guess = int(input("Enter a number between 1 - 100 : "))
    tries +=1

    if guess < secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print(f"😍 Congo! You have guess it in {tries}tries.")