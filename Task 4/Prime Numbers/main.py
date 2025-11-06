import math
Input_list = [10, 501, 22, 37, 100, 999, 87, 351]

# Function to check if a number is prime
def prime(num):

 # Check for divisibility by odd numbers up to the square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# Create a new list to store prime numbers
prime_numbers = []

# Loop through each number and check if it's prime
for num in Input_list:
    if prime(num):
        prime_numbers.append(num)
print(f"Input list:" , Input_list)
print(f"Prime numbers in the list:" , prime_numbers)
print(f"Total count of Prime Numbers in the list:" , len(prime_numbers))
