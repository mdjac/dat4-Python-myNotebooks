from my_modules import utils

utils.get_file_names("/home/jovyan/my_notebooks/my_modules")

utils.get_all_file_names("/home/jovyan/my_notebooks/my_modules")

filenames = ["/home/jovyan/my_notebooks/my_modules/output.txt","/home/jovyan/my_notebooks/my_modules/nytoutput.txt","/home/jovyan/my_notebooks/my_modules/emails.txt"]

utils.print_line_one(filenames)
utils.print_emails(filenames)

md_files = ["/home/jovyan/my_notebooks/my_modules/file1.md","/home/jovyan/my_notebooks/my_modules/file2.md","/home/jovyan/my_notebooks/my_modules/file3.md"]
utils.write_headlines(md_files)