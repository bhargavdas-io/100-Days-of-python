#data types

#Strings      "Hello"
#Integers      123 / 123_456_789 / 123_234.43 (_ is used inplace of comma)
#Booleans      True/False
#Float         3.123


# type() function tells use the type of datatype we are working with
# type casting: str( ) converts numbers to strings
# similarly: float( ) , int( ) etc.

print("please enter a two digit number\n")
num = str (input( ))
sum_of_digits = (int(num[0])+int(num[1]))
print (sum_of_digits)


# Mathematical functions

# ** : exponent. Example: 2**2 = 4
# If there are multiple mathematial operations in a single function, we follow BODMAS and then the calculation is from L to R
# ie. BODMASLR. To change this default priority, we can use brackets as this will change the priority of lower order 
# functions to higher than multiplication, division, Left to Right hierarchy.
# add += 1 will give the same output as add = x + 1. Similarly, we have -=, *=, /=


# round( ) function. round(2.444, 3) : This rounds off 2.44 to 3 decimal places.
# f-Strings: Adding a f infront of the double quotations of a string, we can combine different datatypes in a string.