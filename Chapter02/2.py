print("----- Exercise01 -----")


def print_each_value (values):
    if(len(values) > 0):
        print(values[-1])
        values.pop()
        print_each_value(values)
    else:
        print("DONE")
input_list = [1,2,3,4,5,6,7,8,9,10]
print_each_value(input_list)

print("----- END -----")

print("----- Exercise02 -----")
def concat_names (*names):
    result = ""
    for name in names:
        result += name
    return result

final_names_1 = concat_names("Mikkel","Camilla","Jesper")
final_names_2 = concat_names("Mikkel","Camilla")

print(final_names_1)
print(final_names_2)



print("----- END -----")

