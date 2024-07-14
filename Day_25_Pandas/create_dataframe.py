import pandas
import pandas as pd

## Creating a dataframe from scratch

data_dict = {
    "students": ["Amy","James","Morgan"],
    "scores": [76,56,90]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")