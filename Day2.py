# a :int=3
# b:float=2.5
# c:complex=complex(1,3)

# print(type(a),type(b),type(c))

# breakpoint()

# name="Oscar Shilpakar"

"""-use print(varaible_name[a:b]) to print required string where a and b are starting point and ending point respectively
-use print(variable_name.split(" ")) to split given string
-use variable_name[a] to check what value is in the a position 
-use len(variable name) is used to find the length of the string
-use replace() to replace string
-use name[::-1] to reverse a string
"""
name=input("Enter your name\n")
print(name.split(" "))
print(len(name)) 
splitted_text=name.split(" ")
print(f"First name is {splitted_text[0]}")
print(f"Middle name is {splitted_text[1]}")
print(f"Last name is {splitted_text[2]}")
print(name.replace("oscar","pratistha"))
print(name[::-1])