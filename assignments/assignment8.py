# Explain the difference between the find() and index() methods for strings.

# Python String index() Method allows a user to find the index of the first occurrence of an existing substring inside a given string in Python.For example

string = "Oscar Shilpakar studies in Himalaya College of Engineering"
print("index of 'Himalaya' in string:", string.index('Himalaya'))
# print(string.index("Hello")) uncomment this part to see if it works or not

# The find() method is similar to the index(). The only difference is find() returns -1 if the searched string is not found and index() throws an exception in this case.

print("index of 'Himalaya' in string:", string.find('Himalaya'))
a=string.find("Hello")
print(a)