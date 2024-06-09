import random

rock = '''  .----.-----.-----.-----.
 /      \     \     \       
|  \/    |     |   __L_____L__
|   |    |     |  (            )
|    \___/    /    \______/    |
|        \___/\___/\___/       |
 \      \     /               /
  |                        __/
   \_                   __/
    |        |         |
    |                  |
    |                  |'''


paper = '''         
     /"\|\./|/"
    |\./|   |\./|
    |   |   |   |
    |   |>~<|   |
    |>~<|   |>~<|\./|
    |   |   |   |   |
/~T\|   |           |
|_/ |   |   |   |   |
|   | ~   ~   ~ |   |
|~< |             ~ |
|   '               |
\                   |
 \                 /
  \               /
   \.            /
     |          |
     |          | 
                  '''

scissor = '''
          _______
      ---'   ____)____
                ______)
             __________)
            (____)
      ---.__(___)
'''

images = [rock, paper, scissor]
user = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer_choice = random.randint(0, 2)
print(f"Computer chose:")

if user >= 3 or user < 0:
    print("You typed an invalid number")
else:
    print(images[computer_choice])

    print(images[user])

    if user == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user == 2:
        print("You lose")
    elif computer_choice == user :
        print("Tie")
    elif computer_choice > user :
        print("You lose")
    elif user > computer_choice:
        print("You win!")



