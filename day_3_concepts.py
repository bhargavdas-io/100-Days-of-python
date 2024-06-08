#Conditional Statements
# if/else
# Operators:
# < , > ,>=,<=,!=, == (equalto precisely, this is to check if LHS matches RHS)

# Nested if/else statements

# if condition:
#    if another condition:
#       do A
#    elif:
#       do B
# else:
#       do C


# Logical Operators
# A and B   : Both A , B needs to be satisfied for it to be True
# A or B    : Any one of A , B needs to be satisfied for it to be True
# NOT B     : Reverses the condition. If True, then it becomes False and viz a viz


print("Welcome to roller coaster ride")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print ("Child ticket price is $5.")
    elif age <= 18:
        bill = 8
        print("Youth ticket price is $8.")
    elif age >= 45 and age <= 55 :
        bill = 0
        print("Your ticket is free, sir.")
    elif age <= 45:
        bill = 12
        print("Adult ticket price $12.")
    want_photo = input("Do you want a photo to be taken? 'Y' or 'N'")
    if want_photo == "Y":
        bill += 3
    print(f"Your bill is ${bill}")
else:
    print ("Sorry you are not eligible for the ride")

