#
#traditional method to populate a new list using for loop:

#new_list = []
#for i in numbers:
#    increment = i + 1
#    new_list.append(increment)

#print(new_list)


# using list comprehension:
#numbers = [2, 3, 5, 7]

#new_list = [i+1 for i in numbers]
#print(new_list)

# List comprehension isn't limited to lists, we can also use it with strings,tuples,range:

#name = "Bhargav"

#list_of_letters = [i for i in name]
#print(list_of_letters)


#x = range(1, 5)

#increment = [i*2 for i in x]
#print(increment)

# List comprehension with condition

num = [2, 4, 5, 6, 1, 0]
new_list = [i for i in num if i < 5]
print(new_list)

#ex. 2:

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

upper_cased = [name.upper() for name in names if len(name) >= 5]
print(upper_cased)
