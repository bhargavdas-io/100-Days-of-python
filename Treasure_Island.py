print('''  _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
      ''')

print("Welcome to Treasure Island!")
print("Your mission is to make it out safe!")
print("Choose a path....'left' or 'right'?")
path = input()
in_lower3 = path.lower()
if in_lower3 == "left":
    print("Do you want to 'swim' or 'wait'?")
    route = input()
    in_lower = route.lower()
    if in_lower == "wait":
        print("Choose a door....'red', 'blue' or 'yellow'")
        door = input()
        in_lower2 = door.lower()
        if in_lower2 == "yellow":
            print("You Win..chosen one!")
        elif in_lower2 == "red":
            print("You caught fire!!!! Game over!")
        elif in_lower2 == "blue":
            print("You have been eaten by a bear! Game Over :(")
        else:
            print("Game Over")
    elif in_lower == "swim":
        print ("You have been attacked by a shark! Game over :(")
elif in_lower3 == "right":
    print("You fell into a hole.....game over!")
else:
    print ("Game over")
    
   

