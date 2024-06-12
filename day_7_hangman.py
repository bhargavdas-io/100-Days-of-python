import random
import hangman_art
import hangman_wordlist
chosen_word = random.choice(hangman_wordlist.word_list)

print(hangman_art.logo)


display = []

lives = 6


for _ in range(len(chosen_word)):
    display += "_"


end = False
while not end:  # if end is False, not end is True
                # So, loop will run
    guess = input("Guess a letter \n").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:   
            display[position] = letter
            print(display)
    if guess not in chosen_word:
        print(f"You guessed the letter {guess},thats not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end = True
            print("You lose")
    if "_" not in display:
        end = True
        print("You Win")
    print(hangman_art.stages[lives])






