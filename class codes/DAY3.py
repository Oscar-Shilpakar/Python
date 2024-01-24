"""# string
name="abc123"

# list
names=['a','b','c']

# tuple
ctry=('a','b','c')

# dictionary(Dictionaries are used to store data values in key:value pairs)
user={
    'id':'oscar'
}

# set(cannot add duplicate items in set)
numbs={1,2,3,4,1}

# id()(gives location of variable)
user={
    "name":"Oscar",
    "age":"19",
    "address":"Jombahal",
    "country":"Nepal",
}

# .get() gives value of the key provided
print(user.get("name"))

# .keys() gives keys in the form of list
print(user.keys())

# .values() gives values in the form of list
print(user.values())

# user.setdefault("key","value") adds new key:value pair in the dictionary
user.setdefault("father_name","Ushan")
user["mother_name"]="Saluja"
print(user.keys())
print(user.values())
"""

"""user={}
user["name"]=input("Enter your name: ")
user["age"]=input("Enter your age: ")
user["religion"]=input("Enter your religion: ")
user["father_name"]=input("Enter your father name: ")
user["mother_name"]=input("Enter your mother name: ")
user["college_name"]=input("Enter your college name: ")
print(user)
# using for loop
attr=["name","age","religion","father_name","mother_name","college_name"]
for i in attr:
    user.setdefault(i,input(f"Enter you {i}: "))
print(user)

# set
numbers={1,2,3,4,5,4,3,2,1}
another_nos={0,4,7}
"""