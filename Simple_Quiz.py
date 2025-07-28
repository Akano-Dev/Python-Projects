print("This is a fun quiz")
print("\n")
print("Your current Score is 0")
print("\n")

score = 0

#Question 1
print("1) What is the Capital of India?")
print("A) Maharastra")
print("B) New Delhi")
print("C) Agartala")
print("D) Meghalaya")

answer1 = input("Your Answer: ").upper()

if answer1 == 'B':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect! The correct answer is B")
    print("\n")

#Question 2
print("2) What is the capital of Japan?")
print("A) Seoul")
print("B) Tokyo")
print("C) Beijing")
print("D) Bangkok")

answer2 = input("Your Answer: ").upper()

if answer2 == 'B':
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect! The correct answer is B")
    print("\n")

#Question 3
print("3) Which planet is known as the Red Planet?")
print("A) Earth")
print("B) Venus")
print("C) Mars")
print("D) Jupiter")

answer3 = input("Your answer : ").upper()

if answer3 == 'C':
    score = score + 1
else:
    print("Incorrect! The correct answer is C")
    print("\n")

#Question 4
print("4) How many continents are there?")
print("A) 5")
print("B) 6")
print("C) 8")
print("D) 7")

answer4 = input("Your answer : ").upper()

if answer4 == 'D':
    score = score + 1
else:
    print("Incorrect! The correct answer is D")
    print("\n")

#Display score
print(f"\nYour Score is {score} out of 4")