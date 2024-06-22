# Day 14 Project


import random
import game_data
import art
from game_data import data
from art import vs
from art import logo
score = 0
game_continue = True
selection_b = random.choice(data)
def clear():
    import os
    os.system('cls')

def format_data(selection):
    account_name = selection['name']
    acount_desc = selection['description']
    account_country=selection['country']
    return(f"{account_name}, a {acount_desc}, from {account_country}")

def check_answer(choice,follower_A,follower_B):

    if follower_A > follower_B:
        if choice == "A":
            return choice == "A"               ##### CHECK THIS IN THONNY
    else:
        return choice == "B"



while game_continue:

    ## Randomly select two entities from game_data
    selection_a = selection_b
    selection_b = random.choice(data)
    
    while selection_b == selection_a:
        selection_b = random.choice(data)

    print(logo)


    # Printing comparision prompt for both
    print(f"Compare A: {format_data(selection_a)}.")

    print(vs)

    print(f"Compare B: {format_data(selection_b)}.")

    choice = input("Who has more followers? 'A' or 'B'?: ").upper()
    follower_A = (selection_a['follower_count'])
    follower_B = (selection_b['follower_count'])
    is_correct = check_answer(choice, follower_A,follower_B)

    clear()
    print(logo)

    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score {score}")

