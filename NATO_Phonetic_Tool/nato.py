import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_1 = {row.letter: row.code for (index, row) in data.iterrows()}


def generate():
    word = input("Enter a name: ").upper()
    try:
        output_list = [dict_1[i] for i in word]
    except KeyError:
        print("Please enter alphabets only!")
        generate()

    else:
        print(output_list)


generate()
