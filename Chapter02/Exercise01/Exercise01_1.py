import csv
from pprint import pprint
import argparse

def print_file_content(file):
    with open(file) as f:
        reader = csv.reader(f, delimiter='\t')
        header_row = next(reader)

        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))

def write_list_to_file(output_file, *input_strings):
    with open(output_file, 'a') as file_object:
        for x in input_strings:
            file_object.write(x+ '\n')
       
def read_csv(input_file, print_or_file = None):
    with open(input_file) as f:
        reader = csv.reader(f, delimiter=";")
        output_list = []
        header_row = next(reader)
        output_list.append(header_row)
        for row in reader:
            output_list.append(row)

    if(print_or_file == None):
        pprint(output_list)
    else:
        newline=None
        with open(print_or_file, 'w', newline=newline) as output_file:
            output_writer = csv.writer(output_file)
            for row in output_list:
                output_writer.writerow(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chapter02 Weekly Exercise, can read csv content and print output to screen or save in a file")
    parser.add_argument("CSV",help="path to CSV file")
    parser.add_argument("--file",help="output filename, if empty will print to screen")

    args = parser.parse_args()

    file_location = args.CSV
    write_to_file = args.file

    
    #print_file_content("/home/jovyan/data/country_codes.csv")
    #write_list_to_file("./output.txt","input1","input2","input3")
    read_csv(file_location,write_to_file)