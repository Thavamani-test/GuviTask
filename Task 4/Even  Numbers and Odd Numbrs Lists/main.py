#Given Input List [10, 501, 22, 37, 100, 999, 87, 351]
Input_list = [10, 501, 22, 37, 100, 999, 87, 351]
#Create empty lists for Even and Odd Numbers
even_numbers = []
odd_numbers = []

#Looping to each number and check whether it is even or odd
for n in Input_list:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

print("Input List:", Input_list)
print("Even numbers List:", even_numbers)
print("Odd numbers List:", odd_numbers)
