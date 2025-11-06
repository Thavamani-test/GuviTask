#Given Input List
People = [
    {'name': 'Vainav', 'age': 21},
    {'name': 'Nithya', 'age': 10},
    {'name': 'Dhivya', 'age': 45},
    {'name': 'Gowtham', 'age': 18}
        ]
#Using filter function is to apply on lambda function to filter out, If lambda returns true, that element is included else it will be excluded
Adults=filter(lambda person: person ['age'] >=18, People)
Under18=filter(lambda person: person ['age'] <18, People)

#Using list with map to get the list of people
AdultsList=list(map(lambda person: person ['name'], Adults))
Under18List=list(map(lambda person: person ['name'], Under18))

#Output
print(AdultsList)
print(Under18List)