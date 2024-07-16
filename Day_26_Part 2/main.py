dictionary = {
    "names": ["Bhargav", "Angela", "Kylie"],
    "Age": [56, 72, 29]
}

#Looping throug a dictionary conventionally using loops:

#for (key, value) in dictionary.items():
#    print(key)
#    print(value)


# Looping through a pandas dataframe is similar to looping through a dictionary:
import pandas

df = pandas.DataFrame(dictionary)
#print(df)

#loop:

#for (key, value) in df.items():
#    print(key)
#    print(value)

######## But the above isnt useful as it simply loops through the columns and prints the values.

######## Pandas has a built in loop: method known as iterrows()

######## This loops through each of the rows in the dataframe rather than the columns.

for (index, row) in df.iterrows():
    #print(index)
    #print(row)
    #print(row.names)
    #print(row.Age)
    if row.names == "Bhargav":
        print(row.Age)

# Therefore in Dataframe comprehension: {new_key:new_value for (index, row) in df.iterrows()} , instead of:
# {new_key:new_value for (key, value) in dictionary.items()}
