# Given Input list and target sum value
Input_List = [10, 20, 30, 9]
target_Value = 59

# Setting Flag to check if triplet is found
foundnum = False

# Loop through all triplets
for i in range(len(Input_List)):
    for j in range(i + 1, len(Input_List)):
        for k in range(j + 1, len(Input_List)):
            if Input_List [i] + Input_List [j] + Input_List [k] == target_Value:
                print(f"Triplet found: ({Input_List [i]}, { Input_List [j]}, { Input_List [k]})")
                foundnum = True
