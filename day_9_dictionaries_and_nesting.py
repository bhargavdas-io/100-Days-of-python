#Structure of a dictionary:


#{"key": "value"}

example_dictionary = {"Bug":" A moth in a computer", 
                      "Loop":"Doing a task again and again",
                      "Function":"A piece of code that you can easily call over and over again."
                     }

#adding values in a dictionary:

example_dictionary["index"] = "The index function returns the position of the elements"

#print(example_dictionary)

# Clearing a dictionary:
# An existing dictionary can be cleared simply by taping into the dictionary and using { } braces

clearing_dictionary = {"abc": "alphabets"}

# Clearing it:

clearing_dictionary={}

#print(clearing_dictionary)

# Editing a dictionary:
### Key names are sensitive and also are upper, lower case sensitive.###

example_dictionary["Bug"] = "A computer bug is an issue that prevents a code from running as expected"

#print(example_dictionary)

# Looping in a dictionary:

#for item in example_dictionary:
#    print(item)

# Unlike a list, where we specify the index values to retrieve an item from the list, here it will return the keys only
# To get the items as well as keys
for item in example_dictionary:
    print(item)
    print(example_dictionary[item])

# Also, to create an empty dictionary:
# dictionary_name = {}






