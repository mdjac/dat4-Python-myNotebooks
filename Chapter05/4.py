import pandas as pd
import numpy as np

fname = "./data/51a08a5b-8f06-464e-95df-465f4ccc0677_Data.csv"

data = pd.read_csv(fname)
print(data.head())

#1
data = data.replace("..","")
print(data.head())

#2
data = data.set_index(["Country Name"])
print(data.head())

#3
series_2019 = data["2019 [YR2019]"]
print("2019 series printing",series_2019)

#4
numeric_2019 = pd.to_numeric(series_2019)
print("numeric series printing",numeric_2019)


#5
top10_countries_2019 = numeric_2019.sort_values(ascending=False)
top10_countries_2019 = top10_countries_2019[0:10]
print("task 5")
print(top10_countries_2019)

#6
pop_data = pd.read_csv("./data/05336750-6cf0-4d66-b2b5-28aac387f83d_Data.csv")
pop_data = pop_data.replace("..","")
print("task 6")
print(pop_data.head())
pop_data = pop_data.set_index(["Country Code"])
pop_data_2019 = pop_data["2019 [YR2019]"]
pop_data_2019 = pd.to_numeric(pop_data_2019)
print(pop_data_2019.head())
data = data.merge(pop_data, left_on="Country Code", right_on="Country Code")
print(data.head())

filtered_dataframe = data[["Country Code","2019 [YR2019]_x","2019 [YR2019]_y"]]
filtered_dataframe = filtered_dataframe.set_index(["Country Code"])
filtered_dataframe = filtered_dataframe.replace("",np.nan)
filtered_dataframe = filtered_dataframe.dropna()
filtered_dataframe = filtered_dataframe.rename(columns={"2019 [YR2019]_x":"Mil 2019","2019 [YR2019]_y":"Pop 2019"})
filtered_dataframe = filtered_dataframe.apply(pd.to_numeric)
filtered_dataframe["Mil pr citizen"] = filtered_dataframe["Mil 2019"] / filtered_dataframe["Pop 2019"]
filtered_dataframe = filtered_dataframe.sort_values(by=["Mil pr citizen"], ascending=False)
print(filtered_dataframe.head())
top10_by_mil_citizen = filtered_dataframe[0:10]
print(top10_by_mil_citizen)

#7
list_of_middle_eastern = ['YEM','ARE','TUR','SYR','SAU','QAT','PSE','OMN','LBN','KWT','JOR','ISR','IRQ','IRN','EGY','CYP','BHR']
middle_east = filtered_dataframe[filtered_dataframe.index.isin(list_of_middle_eastern)]
print(middle_east.head())
top3_middle_east = middle_east[0:3]
print(top3_middle_east.head())

