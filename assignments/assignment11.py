# Implement a program that counts the number of vowels in a given string using a loop.

string=input("Enter any string to count number of vowels present in it: ")
count=0
lowered_string=string.lower()
for i in lowered_string:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"): 
        count=count+1
print(f"There are {count} vowels in the string.")