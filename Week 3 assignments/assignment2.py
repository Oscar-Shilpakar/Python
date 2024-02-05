def merge_dicts(dict1,dict2):
    dict1.update(dict2)
    return dict1
dict1={
    "name":"oscar",
    "roll":24,
    "class":"CSIT 3"
}
dict2={
    "name":"oscar",
    "roll":20,
    "class":"CSIT 5",
    "college":"HCOE"
}
merged_dict=merge_dicts(dict1,dict2)
print(merged_dict)