import pandas as pd
import numpy as np


data = np.array([
                ['','Col1','Col2','col3'],
                ['Row1',1,2,3],
                ['Row2',4,5,6],
                ['Row3',7,8,9]
                ])

data = pd.DataFrame(data=data[1:4,1:4], columns=data[0,1:4], index=data[1:4,0])

print(data)


slice_1 = data["Col2"]
print("printing slice1 \n",slice_1.values)
print(type(slice_1))
slice_2 = data.iloc[:,-1]
print("printing slice 2 \n",slice_2)

slice_3 = data.iloc[2,1]
print("printing slice 3 \n",slice_3)


test = pd.DataFrame(data)
print("printing test",test)