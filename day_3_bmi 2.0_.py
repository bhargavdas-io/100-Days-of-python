print("Enter your height in meters:\n")
height = float(input())
print("Enter your weight in kilograms:\n")
weight = float(input())
height_squared = pow(height,2)
print("Calculating BMI...")
bmi = round(weight/height_squared,2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30 :
    print(f"Your BMI is {bmi}, you have are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi},you are obese.")
else:
    print (f"Your BMI is {bmi}, you are clinically obese.")