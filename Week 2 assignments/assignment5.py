# Write a program to remove duplicate elements from a list.

duplicate_numbers=[1,2,3,3,4,5,6,4]
print("initial list: ",duplicate_numbers)
non_duplicated_numbers=[]
for num in duplicate_numbers:
    if(num not in non_duplicated_numbers):
        non_duplicated_numbers.append(num)
print("final list",non_duplicated_numbers)