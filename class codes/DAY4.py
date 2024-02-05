"""# use ** before dictionary name to combine two or more dictionary in one
user1={
    "name":"Oscar",
    "age":"19",
}
user2={
    "address":"Jombahal",
    "country":"Nepal",
}
user_combined={
    **user1,
    **user2,
}
print(user_combined)

# similarly use * to merge list"""

"""numbers=[1,2,3,4,5,6]
def sum_of_list(*args, **kwargs):
    return sum([*list(args),*kwargs.get("nums")])
Sum=sum_of_list(1,2,3,4,5,nums=numbers)
print(f"Sum of numbers is {Sum}")"""

dict={
    "name":"Oscar Shilpakar",
    "number":"9818556408",
}
def merge(*args,**kwargs):
    merged_dict={
        **args[0],
        **kwargs,
    }
    return merged_dict
a=merge(dict,roll_no="24",father_name="Ushan Shilpakar")
print(a)