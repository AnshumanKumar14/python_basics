#Lists are mutable
demo_1 = ['1', '2', '3']
demo_2 = demo_1
demo_1[0] = '3'
print(demo_1)
print(demo_2)

#Tuple -> Immutable
demo_1 = ('1', '2', '3')
demo_2 = ('3','4')

#sets
numbers = {'Math', 'Physics', 'Chemistry', 'Math'}
print('Math' in numbers)