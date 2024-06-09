line1 = ["[ ]","[ ]","[ ]"]
line2 = ["[ ]","[ ]","[ ]"]
line3 = ["[ ]","[ ]","[ ]"]

map = [line1,line2,line3]
print ("Hiding your treasure! X marks the spot!")
position = input()
letter = position[0].lower()      ####### Checks the letter at index 0 of the input. ie. B2 means "B" and change it to lower as "b"
abc = ["a", "b", "c"]
letter_index = abc.index(letter)  ####### Compares the input letter to this list, and gives a integer. ie. If input is B, it will compare the same with the list abc, and since "b" is in position 1, it will give us 1 as the integer.
num_index = int(position[1]) - 1  ####### Same as line 8, index 1 this time. If B2, then its 2.
map[num_index][letter_index] = " X "
print (f"{line1}\n{line2}\n{line3}")