PLACEHOLDER = "[name]"
with open ("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
with open ("./Input/Letters/starting_letter.txt")as letter_file:
    letter_contents = letter_file.read()
    for i in names:
        stripped = i.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped)
        with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt",mode="w") as complete:
            complete.write(new_letter)


