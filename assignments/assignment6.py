# Reverse a given string without using the reverse function or slicing

string="oscar"
print("Original string is",string)
string_length=len(string)
reverse_string=""
for s in string:
    reverse_string=reverse_string+string[string_length-1]
    string_length-=1
print("Reversed string is",reverse_string)
