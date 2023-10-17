import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = data["Primary Fur Color"][data["Primary Fur Color"] == "Gray"].count()
black_count = data["Primary Fur Color"][data["Primary Fur Color"] == "Black"].count()
cinnamon_count = data["Primary Fur Color"][data["Primary Fur Color"] == "Cinnamon"].count()
print(gray_count)
print(black_count)
print(cinnamon_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_count, black_count, cinnamon_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
