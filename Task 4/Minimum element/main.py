#Get Input from the user
Input_List= list(map (int, input("Enter the List of Numbers separated by spaces: ").split()))

print(f" Enter the List of Numbers: ", Input_List)

#Find the minimum element
min_element = min(Input_List)

#Output Display
print(f" Minimum Element in the List: ",min_element)
