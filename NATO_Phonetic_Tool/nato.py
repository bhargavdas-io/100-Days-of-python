import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_1 = {row.letter:row.code for (index, row) in data.iterrows()}

word = input("Enter a name: ").upper()
output_list = [dict_1[i] for i in word]
print(output_list)




