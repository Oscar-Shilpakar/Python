# Write a Python program to check if a given string is a palindrome.

string=input("Enter any string to check whether it is palindrome or not: ")
string_length=len(string)
reverse_string=""
for s in string:
    reverse_string=reverse_string+string[string_length-1]
    string_length-=1
if(reverse_string==string):
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")
     