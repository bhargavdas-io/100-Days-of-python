import guess_art
import random
from guess_art import logo

print(logo)
EASY_LEVEL = 10
HARD_LEVEL = 5


print ("! Welcome to the Number Guessing Game !")
print("I am thinking of a number between 1 and 100..... ")

number_list = list(range(1, 101))

answer = random.choice(number_list)  # Generates a random number from the list between 1 to 100
print(answer)



def set_difficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL
    
def check_answer(guess,answer, turns):
                                                #### Check
    if guess > answer:
        print("Too high")
        return turns - 1
    elif guess < answer:
        print("Too less")
        return turns - 1
    else:
        print(f"You got the correct answer {answer}")


turns = set_difficulty()



guess = 0
while guess != answer or turns == 0:
    print(f"You have {turns} attempts left.")
    guess = int(input("Guess the number: "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
        print("You ran out of guesses.")
