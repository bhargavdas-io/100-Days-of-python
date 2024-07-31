## Dictionary comprehension using a list

#my_dict = {new_key:new_value for i in list}

## Dictionary comprehension using an existing dictionary

# dict_1={
#    key:value,
#    key:value
#        }

#my_dict = {new_key: new_value for (key,value) in dict_1.items()}

## Conditional dictionary comprehension:

# new_dict = {new_key:new_value for (key, value)  in dict.items() if test}


## Dictionary comprehension with list example:

import random

students = ["Bhargav", "Kaustav", "Bhargab K.", "Nikhil", "Chirag"]
marks_dict = {i: random.randint(0, 100) for i in students}

# dictionary comprehension with condition
passed_students = {i: score for (i, score) in marks_dict.items() if score >= 50}
print(passed_students)

