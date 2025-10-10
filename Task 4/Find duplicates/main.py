#Three Input sample lists
list1= [11, 101, 48, 90, 55, 83]
list2 = [30, 48, 55, 63, 12, 83, 95]
list3 = [55, 77, 83, 90, 10, 14]

#Find duplicates
set_intersection = list(set(list1) & set(list2) & set(list3))

#Display Output
print(f"List1:", list1)
print(f"List2:", list2)
print(f"List3:", list3)
print(f"Duplicates from all three lists:", (set_intersection))
