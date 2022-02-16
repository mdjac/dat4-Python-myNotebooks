print("----- EXERCISE 01 -----")
import os

dirs = os.listdir("./")
print(dirs)


print("----- END -----")


print("----- EXERCISE 02 -----")
filename = "./inputfile.txt"
with open(filename, "r") as i_f:
    lines = i_f.readlines()
print(lines)

lines_starting_with_number = []

for line in lines:
    f_character = line[0]
    if(f_character.isdigit()):
        lines_starting_with_number.append(line)

print(lines_starting_with_number)

newfilename = "./outputfile.txt"
with open(newfilename, "w") as o_f:
    for newline in lines_starting_with_number:
        o_f.write(newline)

print("----- END -----")


print("----- EXERCISE 03 -----")

import glob
folders = glob.glob("./**/*.txt", recursive=True)
for name in folders:
    print(os.path.abspath(name))
print("----- END -----")

print("----- EXERCISE 02-1 -----")
import openpyxl

# created from: https://en.wikipedia.org/wiki/Iris_flower_data_set#Data_set
filename = '/home/jovyan/data/iris_data.xlsx'
wb = openpyxl.load_workbook(filename)
print(wb.sheetnames)
sheet = wb.get_sheet_by_name("Fisher's Iris Data")

data = []

for rowOfCellObjects in sheet:
    data_row = []
    for cellObject in rowOfCellObjects:
        data_row.append(cellObject.value)
    data.append(data_row)

import csv
newline=None
with open('./outputCSV.csv', 'w', newline=newline) as output_file:
    output_writer = csv.writer(output_file)
    
    for row in data:
        output_writer.writerow(row)

print("----- END -----")

print("----- EXERCISE 02-2 -----")
filename = '/home/jovyan/data/befkbhalderstatkode.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    import pprint
    final_dict = {}
    dict_statcode_persons = {}
    dict_age_statecode_persons = {}
    dict_group_age_statecode_persons = {}
    for row in reader:
        dict_statcode_persons[row[3]] = row[4]
        dict_age_statecode_persons[row[2]] = dict_statcode_persons
        dict_group_age_statecode_persons[row[1]] = dict_age_statecode_persons
        final_dict[row[0]] = dict_group_age_statecode_persons
        if reader.line_num > 50000:
            break

    with open('./kkdata.py', 'w') as out_file:
        out_file.write('STATISTICS =' + pprint.pformat(final_dict))

print("----- END -----")


