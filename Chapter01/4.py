print("----- Exercise -----")




def translate_date (input):
    months_numbers = {"JAN":1,"FEB":2,"MAR":3,"APR":4,"MAY":5,"JUN":6,"JUL":7,"AUG":8,"SEP":9,"OCT":10,"NOV":11,"DEC":12}


    splitted_string = input.split("-")


    splitted_string[1] = months_numbers[splitted_string[1]]

    final_tuple = tuple(splitted_string)

    final_string = "".join(str(final_tuple))

    return final_string

initial_date= "18-FEB-85";
print(translate_date(initial_date))

print("----- END -----")