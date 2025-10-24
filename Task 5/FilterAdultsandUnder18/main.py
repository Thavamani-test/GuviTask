People = [
    {'name': 'Vainav', 'age': 21},
    {'name': 'Nithya', 'age': 10},
    {'name': 'Dhivya', 'age': 45},
    {'name': 'Gowtham', 'age': 18}
        ]

Adults=filter(lambda person: person ['age'] >=18, People)
Under18=filter(lambda person: person ['age']<18, People)

AdultList=list(map(lambda person: person ['name'],Adults))
Under18List=list(map(lambda person: person ['name'],Under18))

print(AdultList)
print(Under18List)
