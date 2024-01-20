# Write a Python program to print the Fibonacci sequence up to a certain number using a loop. 

fibonacci_sequence=[0,1]
a=0
b=1
i=0
n=int(input("Enter upto how many terms do you want to go in the sequence: "))
while(i!=(n-2)):
    next_term=fibonacci_sequence[a]+fibonacci_sequence[b]
    fibonacci_sequence.append(next_term)
    a+=1
    b+=1
    i+=1
print(fibonacci_sequence)