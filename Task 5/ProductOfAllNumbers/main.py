#importing reduce function from functools module
from functools import reduce

#Given Input list
Input_List=[5, 2, 9, 3, 1]

product=reduce(lambda x,y:x*y, Input_List)

#Output
print("Product Of All Numbers:", product)