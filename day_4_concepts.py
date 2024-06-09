# Randomisation
# 

#import random
#random_integer = random.randint(1, 10)
#print (random_integer)

# Random floating point numbers:
# 0.000000 to 0.9999999999
# random( ) takes no arguments. So to generate specified random numbers in between a specified range:

#random_float = random.random()
#random_integer * 5 # Gives a random number between 0.0000 to 4.9999999, but not including 5
#print(random_float)

# Lists
# It is way of storing and organising data in python.
# Lists can contain mixed data types as well.
# fruits_and_mix = [1, 0.3, true, "apple"]

states_of_India = ["Assam","Bihar","Maharashtra","West Bengal","Delhi","Tamil Nadu"]
states_of_India[1] = "Arunachal Pradesh"
print (states_of_India[1])
print (states_of_India[-1])

# .append( ) function : appends a new entry to the end of a list

states_of_India.append("Orissa")
print(states_of_India)


# Nested Lists
# fruits = ["Apple","Banana"]
# vegetables = ["Tomato","Spinach"]
# eatables = [fruits,vegetables]        <- nested list