# num_1 = 25
# num_2 = 28
# print(num_1 < num_2)

print("Please enter your name.")
name = input()
print("Please enter your age.")
age = int(input())

if name == "Anshuman" and age == 25:
    print('Hello anshuman.')
elif not name == "Anshuman" and age == 25:
    print('Hello world.')
elif name == "Satya":
    print('Howdy Satya')
else:
    print('Who are you?')