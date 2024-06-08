print("Welcome to pizza deliveries")
print("What size of pizza? S, M or L?")
size = input()
bill = 0
add_pepperoni = input()
extra_cheese = input()
if size == "S":
    bill += 15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print("Thankyou for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}")