from functools import reduce

Input_List=[5, 2, 9, 3, 1]
product=reduce(lambda x,y:x*y, Input_List)

print("Product Of All Numbers:", product)