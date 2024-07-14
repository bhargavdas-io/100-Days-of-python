import pandas as pd
data = pd.read_csv("squirrel_data.csv")
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey_squirrels,cinnamon_squirrels,black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



