# Create a program that uses a loop to print the multiplication table of a given number. 

num=int(input("Enter a number you want to see multiplication table of: "))
i=int(1)
while(i<=10):
    print(f"{num}x{i}={num*i}")
    i+=1