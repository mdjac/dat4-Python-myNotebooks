import numpy as np

data = np.arange(1,101).reshape(10,10)

print(data)

mask = data%2 == 0
exercise1 = data[mask]
print("apply a mask that will return only the even numbers",exercise1)

#b = data.astype('U32')

exercise2 = np.where(data%10 == 6)
print("using np.where() return only numbers that ends with 6",data[exercise2])

