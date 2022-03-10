import pandas as pd

data = pd.read_excel("unisex_names.xls", header=None)
data = data.squeeze()
data = data.tolist()
print(data)

def names_generator(names):
    index = 0
    while index < len(names):
        yield names[index]
        index += 1

test = names_generator(data)
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))

        

