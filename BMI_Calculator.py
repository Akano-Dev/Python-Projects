#BMI Calculator

print("Thi is a BMI calculator")
print("\n")

Info = input("Enter Name : ")
print("\n")

weight = float(input("Enter Weight : "))
print("\n")

height = float(input("Enter Height : "))
print("\n")

def BMI (x,y):
    return x/y

BMI = weight/height
if height == '0':
    print("Invalid")
else:
    print(f"BMI is {BMI}")
