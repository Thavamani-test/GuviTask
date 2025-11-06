#Given list of numbers as an Input
Input_List=[1, 2, 3, 4, 5, 6, 7, 8, 9]

#Using Lambda function to check whether the number is even or not
even_number = lambda x : x % 2 ==0

#Using List comprehension to check each number with the even num list and square it and store in a new list
square_of_even_numbers = [x ** 2 for x in Input_List if even_number(x)]

#Output
print("Input_List : ",Input_List)
print("Even Numbers : ",square_of_even_numbers)