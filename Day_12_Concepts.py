#################### Global scope, Local Scope and Block Scope ###############################


# Local scopes is the concept where a variable is accesable only within the function to which it belongs
# Global scopes is where we declare a variable outside a function and it can be accessed anywhere in the program.
# Block Scope: In python, there is no block scope. Block Scope is when a variable is created within
# if statements, while loops, for loops etc. Variables created within these, can also be accessed anywhere in the program.
#
#
#
# Example of block scope:
#
#if 10 > 5:
#    y = "Hello"
#    print(y)

#print (y)  #### This will also get executed, even if its declared within the if block.



### Modifying Global variables:


# If we want to modify a global variable, we can use the word "global" to explicitly tell the program its a global one.

# Example: 
#
#enemies = 1
#def increment():
#    enemies += 2
#    print(enemies)

#increment()

# The above block of code will not execute.As the program expects to have the enemies variable inside the function before increasing its value.
# To still tap into the variable, we can use th word global:

#enemies = 1
#def increment():
#    global enemies
#    enemies += 2
#    print(enemies)

#increment()

# But this method is not recommended. Instead we can use return.

enemies = 1
def increment():
    return enemies + 1


enemies = increment()
print (enemies)



#
#
# Global constants

# Global constants are values that never needs to be changed like
# value of pi, username, url etc etc.

# As a general convention, in python, global constants are put in 
# variables, where the variable names are all uppercase.

# example:
#PI = 3.14
#URL_GOOGLE = "https://www.google.com"




