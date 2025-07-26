import math

def add(x,y):
    return x + y

def substract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if (y==0):
        print("Invalid Operation")
    return x / y

print("Select Operation : ")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter (1/2/3/4) : ")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

if choice == '1':
    print("Result",add(num1, num2))

elif choice == '2':
    print("Result",substract(num1,num2))

elif choice == '3':
    print("Result",multiply(num1,num2))

elif choice == '4':
    print("Result",divide(num1,num2))

else:
    print("Invalid")