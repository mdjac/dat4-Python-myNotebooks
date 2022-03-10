import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use("pdf")


dates = pd.date_range('20200602', periods=6) # create 6 dates from september 2nd, 2020.
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD')) # use np.random.randn to generate a dataframe of 6 by 4 random numbers
print(dates)
print(df)

print(df.describe())


#A
mean_dict = {}
print("exercise A")
for column in df.columns:
    mean_dict[column] = df[column].mean()
print(mean_dict)

#B
print("Exercise B")
sum_dict = {}
for index, row in df.iterrows():
    sum_dict[index] = row.sum()
new_df = pd.DataFrame(data=sum_dict.values(),index=sum_dict.keys(),columns=["Sum"])
print(new_df)
new_df = new_df.sort_values("Sum",ascending=False)
print(new_df)


#C
print("Exercise C")
new_df = df[(df["A"] > 0) & (df["B"] > 0)]
print(new_df)
