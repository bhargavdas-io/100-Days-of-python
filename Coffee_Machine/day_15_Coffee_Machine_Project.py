MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

print(f"TODAY'S MENU \n")
print(
    f"Espresso : ${MENU['espresso']['cost']}\nLatte: ${MENU['latte']['cost']}\nCappuccino: ${MENU['cappuccino']['cost']} ")



def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item} for the order ")
            return False
    return True

def coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name}! Enjoy")

def process_coins():
    print("Please insert coins:")
    total = int(input("Quarters?: ")) *0.25
    total += int(input("Dimes?: ")) *0.1
    total += int(input("Nickels?: ")) *0.05
    total += int(input("Pennies?: ")) *0.01
    return total

def transaction_success(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved-drink_cost,2)
        print(f"Here is the ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry. That's not enough money. Refund initiated.")
        return False



is_on = True

choice = input("What would you like?(espresso/latte/cappuccino: )")
if choice == "off":
    is_on = False
elif choice == "report":
    print(f"Water: {resources['water']}ml\n,Milk: {resources['milk']}ml\n, Coffee: {resources['coffee']}gm")
else:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        if transaction_success(payment,drink["cost"]):
            coffee(choice,drink["ingredients"])














