# WAP to demonstrate the use case of insert() and extend() methods in Python lists. 

# use case of insert()
name1=[]
i=int(0)
n1=int(input("Enter how many names to insert: "))
while(i<n1):
    a=input("Enter name you want to insert: ")
    name1.insert(0,a)
    i+=1
print(name1)

# use case of extend()
name2=[]
j=0
n2=input("Do you need to add any more names?(Y/N)\n")
n3=int(input("Enter how many names to insert: "))
while(j<n3):
    if(n2=="Y"):
        appended_name=input("enter name you want to add in the list: ")
        name2.insert(0,appended_name)
    j+=1
name1.extend(name2)
print(name1)