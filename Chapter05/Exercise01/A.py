import pandas as pd

data = pd.read_csv("./data/A.csv", delimiter=";")
divorced_2008_sum = data.loc[data["TID"].str.contains("2008")]["INDHOLD"].sum()
divorced_2020_sum = data.loc[data["TID"].str.contains("2020")]["INDHOLD"].sum()

print(data)

print(divorced_2008_sum)
print(divorced_2020_sum)

#tal1 - tal2 = y
#(y / tal2) * 100 =x%
y = divorced_2020_sum - divorced_2008_sum
result = (y / divorced_2008_sum) * 100

print(result)