#importing datetime class from datetime module
from datetime import datetime

#Creating an object for the datetime class and passing values in the datetime format
dt_time = datetime(2025, 10, 27, 11, 50, 30)

#Fetching day, month and year values from the datetime
day = dt_time.day
month = dt_time.month
year = dt_time.year

#Output
print("Date Time:", dt_time)
print("Day :", day)
print("Month:", month)
print("Year:", year)
