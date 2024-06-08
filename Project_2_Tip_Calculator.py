print ("Welcome to tip calculator")
bill = float(input("What was the total bill?"+" $"))
tip = int(input("How much tip would you like to pay? 10%, 12%, or 15%?\n"))
people = int(input("How many people to split the bill?\n"))
#tip_percent = float(tip/100)
tip_calculated = (tip / 100 * bill + bill)/people
rounded_tip = round(tip_calculated,2)
#final_bill = round(float(bill+rounded_tip))
print (f"Each person should pay: ${rounded_tip}")
