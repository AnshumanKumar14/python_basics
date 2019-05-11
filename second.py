# Split function
names = 'anshuman, satya, shikha, dipkia'
print(names.split(','))

#List and dictionary type
userinfolist = ['anshu','29','male','gurgaon']
userinfodict = {'name': 'Anshu', 'age': 29}

# Formatting in python using .format
# My informatio
firstname = 'Anshuman'
lastname = 'Tiwari'
fullname = firstname + ' ' + lastname
age = 29
location = 'Gurgaon'
office = 'Sapient'

# This is used for formatting a string
# First way - Simple .format
myinfo = 'My information is -> Fullname: {}, Age: {}, Location: {}, Office: {}' .format(fullname, age, location, office)
print(myinfo) #This will print my information

#Second way -> Fstring
myinfo = f'My information is -> Fullname: {fullname}, Age: {age}, Location: {location}, Office: {office}'