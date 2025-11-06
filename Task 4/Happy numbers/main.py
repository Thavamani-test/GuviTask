# Given Input list
Input_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is a happy number
def happy_number(n):
    checkednum = set()  # to store numbers already seen in the process
    while n != 1 and n not in checkednum:
        checkednum.add(n)
        n = sum(int(i)**2 for i in str(n))  # sum of squares of digits
    return n == 1

# Create a list to store happy numbers
happy_numbers = []

# Loop through each number and check if it’s happy
for num in Input_list:
    if happy_number(num):
        happy_numbers.append(num)

# Display results
print(f"Input List:", Input_list)
print(f"Happy Numbers List:", happy_numbers)
print(f"Total Count of Happy Numbers:", len(happy_numbers))
