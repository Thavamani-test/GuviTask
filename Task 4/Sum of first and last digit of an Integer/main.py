#Get Input from the user
number= int(input("Enter your number:-"))

#Convert number to string to access the digits easily
number_str = str(abs(number)) #abs() handles negative numbers

#Storing first and last digit
first_digit = int(number_str[0])
last_digit = int(number_str[-1])

#Sum of first and last digits
Sum_of_digits = first_digit + last_digit
#Display Result
print (f"First digit is", first_digit)
print (f"Last digit is", last_digit)
print (f"Sum of first digit and last digit is", Sum_of_digits)
