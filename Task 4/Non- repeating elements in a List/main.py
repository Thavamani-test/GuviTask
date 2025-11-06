# Given list of integers
List_of_numbers = [10, 20, 30, 20, 10, 40, 50, 30, 60, 10]

# Create a list to store non-repeating elements
non_repeating = []

# Loop through each element
for n in List_of_numbers:
    if List_of_numbers.count(n) == 1: # appears only once
        non_repeating.append(n)

# Display Output
print("Input List:", List_of_numbers)
print("Non-Repeating Elements:", non_repeating)
