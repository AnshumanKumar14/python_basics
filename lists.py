#Will return the length of list - Here it will output 4
courses = ['Math', 'Physics', 'Chemistry', 'Hindi']
print(len(courses))
print('\n')

#Appened the data at the end of list
courses.append('IT') 
print(courses)
print('\n')

#Will insert a value at the provided index
courses.insert(0, 'Biology')
print(courses)
print('\n')

#Extend a list with another list
anothercourses = ['C++', 'Python', 'Java']
courses.extend(anothercourses)
print(courses)
print('\n')

#Remove an element from the list
courses.remove('C++')
print(courses)

#Removes the last element from a list
courses.pop()
print(courses)

#Sort the elements of lists
courses.sort()
print(courses)

#Sorted return the sorted version of list but doesn't modify the existing list
anotherlist = sorted(courses)
print(anotherlist)

#Returns the index of input element from the list
indexofIT = courses.index('IT')
print(indexofIT)

#Iterate over the element of the list
for course in courses:
    print(course)

#Enumerate also iterates over the list but also returns the index of the element
for index, course_1 in enumerate(courses):
    print(index, course_1)

#Joins a list
print((', ').join(courses))