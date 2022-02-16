import glob
import os


def get_file_names(folderpath,out="output.txt"):
    """ takes a path to a folder and writes all filenames in the folder to a specified output file"""
    print("get_file_names")
    files = glob.glob(folderpath+"/*.*")
    with open(out, "w") as o_f:
        for file in files:
            o_f.write(os.path.abspath(file)+"\n")

def get_all_file_names(folderpath,out="output.txt"):
    """takes a path to a folder and write all filenames recursively (files of all sub folders to)"""
    print("get_all_file_names")
    files = glob.glob(folderpath+"/**/*.*", recursive=True)
    with open(out, "w") as o_f:
        for file in files:
            o_f.write(os.path.abspath(file)+"\n")


def print_line_one(file_names):
    """takes a list of filenames and print the first line of each"""
    print("print_line_one")
    for file in file_names:
        with open(file) as file_object:
            firstline = file_object.readline()
            print("Filename: ",file,"First line: ",firstline)

def print_emails(file_names):
    """takes a list of filenames and print each line that contains an email (just look for @)"""
    print("Looking for @ now!")
    for file in file_names:
        with open(file) as file_object:
            for line in file_object:
                if("@" in line):
                    print("Filename: ",file,"Contains @: ",line)


def write_headlines(md_files, out="output.txt"):
    """takes a list of md files and writes all headlines (lines starting with #) to a file"""
    print("Looking for #HEADLINES now!")
    headlines = []
    for file in md_files:
        with open(file) as file_object:
            for line in file_object:
                if(line.startswith("#")):
                    headlines.append(line)
    
    #Now write to output file
    with open(out, "w") as o_f:
        for headline in headlines:
            o_f.write(headline+"\n")

if __name__ == "__main__":
    get_file_names("./")

    get_all_file_names("./")

    filenames = ["./output.txt","./nytoutput.txt","./emails.txt"]

    print_line_one(filenames)
    print_emails(filenames)

    md_files = ["./file1.md","./file2.md","./file3.md"]
    write_headlines(md_files)
