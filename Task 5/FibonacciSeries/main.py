#importing reduce function from functools module
from functools import reduce

# Using lambda function to generate Fibonacci series up to n terms
fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n - 2), [0, 1])

#Output
print("Fibonacci Series: ",fib(8))
