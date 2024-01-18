"""Write a Python program that acts as a simple arithmetic calculator. The program should prompt the user to enter two numbers and an arithmetic operation (addition, subtraction, multiplication, or division). Based on the user's input, the program should perform the corresponding operation and display the result. Ensure proper handling of division by zero.
"""

num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
n=int(0)
while(n!=5):
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    n=int(input("Enter which operation you want to perform: "))
    if(n==1):
        print(f"Sum of {num1} and {num2} is {num1+num2}")
    if(n==2):
        print(f"Difference of {num1} and {num2} is {num1-num2}")
    if(n==3):
        print(f"Product of {num1} and {num2} is {num1*num2}")
    if(n==4):
        print(f"Division of {num1} and {num2} is {num1/num2}")
    
    
        