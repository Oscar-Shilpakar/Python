# recursive function in python

# calculating the factorial of x where x >= 1

"""def factorial_func(x):
    #  isinstance => 
    if not isinstance(x, int):
        return "Illegal value provided"
    if x < 1 :
        return "Value cannot be less than 1"
    if x==1:
        return 1
    else:
        return x*factorial_func(x-1)
print(factorial_func(5))
print(factorial_func(-1))
print(factorial_func(1))
print(factorial_func("abc"))"""

# A lambda function is a small anonymous function 

# A lambda function can take any number of arguments, but can only have only one expression

"""y = lambda a,b,c : a+b+c if a<6 else a-b+c
print(y(6,5,5))
fact = lambda n : n*fact(n-1) if n>1 else 1
# print(fact(5))"""

# exception handling

"""try: 
    print("Trying to execute value")
    ret = fact("1")
    print(ret)
except Exception as e:
    print("Exception occured")
    print(f"Exception detail: \n {e.args}")
finally:
    print("Function execution complete")"""

# mapped

"""students=[
    {"name":"oscar","age":"19"},
    {"name":"ronit","age":"18"}
]

mapped= map(lambda x:{"age":x['age']},students)
mapped = list(mapped)
print(mapped)
"""
# filter

"""students=[
    {"name":"oscar","age":"19"},
    {"name":"ronit","age":"18"}
]

fv=filter(lambda y : "n" in y["name"], students)
fv=list(fv)
print(fv)"""

# WAP to take 10 students details from terminal (name,age,religion). make a dictionary for every student and push all items to a list of students. Transform list of students dict to list fo dict with names only. Filter list of students of age 20.

students = []
for i in range(3):
    name = input("Enter name: ")
    age = int(input("Enter age: ")) 
    religion = input("Enter religion: ")
    
    student = {'name':name, 'age':age, 'religion':religion}
    students.append(student)

names = map(lambda s:{'name':s['name']},students)
names=list(map)

twenty_year_olds = filter(lambda s:s['age']==20,students)
twenty_year_olds=list(twenty_year_olds)

print(students)
print(names)
print(twenty_year_olds)
