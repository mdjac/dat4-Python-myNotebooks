import pandas as pd
from collections import defaultdict

data = pd.read_csv("./data/B.csv", delimiter=";")
data = data.drop(columns=["TID"])

print(data)

test = data.groupby(["OMRÅDE","CIVILSTAND"]).sum()
test["INDHOLD"].apply(pd.to_numeric)


print(test)


#Creates DICT
tmp_dict = {}
for index, row in test.iterrows():
    second_dict = tmp_dict.setdefault(index[0],{})
    second_dict[index[1]] = row["INDHOLD"]

#Creates final dataframe
final_df = pd.DataFrame(
    [],
    index=[],
    columns=["Ugift","I alt","Percentage"])
    
for key, value in tmp_dict.items():
    ugift = value.get("Ugift")
    i_alt = value.get("I alt")
    percentage = (ugift / i_alt) * 100
    final_df.loc[key] = [ugift,i_alt,percentage]

final_df = final_df.sort_values(["Percentage"],ascending=False)
print(final_df)

    


 
