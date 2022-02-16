print("----- Exercise01 A -----")
input_names = ["Mikkel","henrik","Hans","Niels","Henriette"]

names_starting_with_h = [name for name in input_names if name[0].upper() == "H"]

print(names_starting_with_h)

print("----- END -----")


print("----- Exercise01 B -----")

numbers_power_3 = [number**3 for number in range(1,101)]

print(numbers_power_3)

print("----- END -----")

print("----- Exercise01 C -----")
names = ["Torben","Jens","Ole","Per"]

list_of_tuples = [tuple([len(name),name]) for name in names]

print(list_of_tuples)

print("----- END -----")

print("----- Exercise01 D -----")
input_string = "123akdsakdkkdqwjeqwjeq8812381###213913919319kasdksakdsakdkadkasdkk!!!!€€))"

numeric_string = "".join([c for c in input_string if c.isnumeric()])
print(numeric_string)
print("----- END -----")


print("----- Exercise01 E -----")
dice_1 = [1,2,3,4,5,6]
dice_2 = dice_1.copy()

result = set([d1+d2 for d1 in dice_1 for d2 in dice_2])
list_of_tuples = sorted(set([tuple(sorted([d1,d2])) for d1 in dice_1 for d2 in dice_2]))


print(list_of_tuples)

print("----- END -----")


print("----- Exercise02 A -----")
names = ["Mikkel","Camilla","Jesper","Matias","Gitte","mikkel"]

names_dict = {k:len(k) for k in names}

print(names_dict)


print("----- END -----")


print("----- Exercise02 B -----")
numbers = [0,1,2,3,4,5]

import math

numbers_dict = {n:math.sqrt(n) for n in numbers}

print(numbers_dict)

print("----- END -----")

print("----- Exercise03 -----")
times_of_each_sum = sorted([d1+d2 for d1 in dice_1 for d2 in dice_2])



final_dict = {}
for number in times_of_each_sum:
    final_dict.setdefault(number,0)
    final_dict[number] += 1

result_dict = {k:(v/len(times_of_each_sum)*100) for (k,v) in final_dict.items()}
from pprint import pprint
print(final_dict)

pprint(result_dict)
print("Total sum of percentage: ",sum(result_dict.values()))
print("----- END -----")





