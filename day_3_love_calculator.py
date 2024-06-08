print("Welcome to Love Calculator")
print("Enter first name")
name_1 = input()
print("Enter second name")
name_2 = input()
combined_name = name_1 + name_2
lower_names = combined_name.lower()
t = lower_names.count("t")
r =lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")

first_digit = t+r+u+e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")

second_digit = l+o+v+e
score = int(str(first_digit)+str(second_digit)) ###

if (score < 10) or (score > 90) :
    print(f"Your score is {score}, you go like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")


