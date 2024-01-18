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
# name=input("Enter your name\n")
# print(name.split(" "))
# print(len(name)) 
# splitted_text=name.split(" ")
# print(f"First name is {splitted_text[0]}")
# print(f"Middle name is {splitted_text[1]}")
# print(f"Last name is {splitted_text[2]}")
# print(name.replace("oscar","pratistha"))
# print(name[::-1])

# girlfriends=["one","and","only","the","great","pratistha"]
# print(f"my girlfriend {girlfriends}")
# girlfriend_count=len(girlfriends)
# print(girlfriend_count)

# girlfriends=["one","and","only","the","great","pratistha"]
# for i in girlfriends:
#     print(i)
# i=0
# while(i<=5):
#     print(i)
#     i+=1

"""WAP in such a way that when user enters input 'ram' as a name break loop and print the list otherwise keep on appending items to list amd ask for next input from terminal"""

name_list=[""]
while(name_list[-1]!="ram"):
    name=input("Enter name: ")
    name_list.append(name)
print(name_list[1:])