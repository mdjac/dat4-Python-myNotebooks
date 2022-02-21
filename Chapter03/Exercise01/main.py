from classes import *
import names
import random
import csv
from pprint import pprint
import matplotlib as mpl
import matplotlib.pyplot as plt

course1 = Course("Coursename 1","Room 1","Teacher 1",random.randint(8,25))
course2 = Course("Coursename 2","Room 2","Teacher 2",random.randint(8,25))
course3 = Course("Coursename 3","Room 3","Teacher 3",random.randint(8,25))
course4 = Course("Coursename 4","Room 4","Teacher 4",random.randint(8,25))
course5 = Course("Coursename 5","Room 5","Teacher 5",random.randint(8,25))
course6 = Course("Coursename 6","Room 6","Teacher 6",random.randint(8,25))
course7 = Course("Coursename 7","Room 7","Teacher 7",random.randint(8,25))
course8 = Course("Coursename 8","Room 8","Teacher 8",random.randint(8,25))
course9 = Course("Coursename 9","Room 9","Teacher 9",random.randint(8,25))
course10 = Course("Coursename 10","Room 10","Teacher 10",random.randint(8,25))
course11 = Course("Coursename 11","Room 8","Teacher 8",random.randint(8,25))
course12 = Course("Coursename 12","Room 8","Teacher 8",random.randint(8,25))
course13 = Course("Coursename 13","Room 8","Teacher 8",random.randint(8,25))
course14 = Course("Coursename 14","Room 8","Teacher 8",random.randint(8,25))
course15 = Course("Coursename 15","Room 8","Teacher 8",random.randint(8,25))
course16 = Course("Coursename 16","Room 8","Teacher 8",random.randint(8,25))
course17 = Course("Coursename 17","Room 8","Teacher 8",random.randint(8,25))
course18 = Course("Coursename 18","Room 8","Teacher 8",random.randint(8,25))
course19 = Course("Coursename 19","Room 8","Teacher 8",random.randint(8,25))
course20 = Course("Coursename 20","Room 8","Teacher 8",random.randint(8,25))
course21 = Course("Coursename 21","Room 8","Teacher 8",random.randint(8,25))
course22 = Course("Coursename 22","Room 8","Teacher 8",random.randint(8,25))
course23 = Course("Coursename 23","Room 8","Teacher 8",random.randint(8,25))
course24 = Course("Coursename 24","Room 8","Teacher 8",random.randint(8,25))

datasheet1 = DataSheet()
datasheet2 = DataSheet()
datasheet3 = DataSheet()
datasheet4 = DataSheet()
datasheet5 = DataSheet()

students = []

def random_generator_and_output():

    


    
    datasheets = [datasheet1,datasheet2,datasheet3,datasheet4,datasheet5]
    courses = [course1,course2,course3,course4,course5,course6,course7,course8,course9,course10,course11,course12,course13,course14,course15,course16,course17,course18,course19,course20,course21,course22,course23,course24]
    possible_grades = [0,2,4,7,10,12,None]

    #Makes random assignment to datasheets with courses and grades
    while len(courses) > 0:
        course_idx = random.randint(0,len(courses)-1)
        sheet = random.choice(datasheets)
        courses[course_idx].set_grade(random.choice(possible_grades))
        sheet.add_course(courses[course_idx])
        courses.pop(course_idx)


    #Creates the students
    #while len(datasheets) > 0:
    for i in range(0,len(datasheets)):
        gender_based = random.randint(0,1)
        name = ""
        if gender_based == 0:
            #Male
            name = names.get_full_name(gender='male')
            gender = "Male"
        if gender_based == 1:
            #Female
            name = names.get_full_name(gender='female')
            gender = "Female"
        sheet = random.choice(datasheets)
        new_student = Student(name,gender,"Gider ikke lave random url",sheet)
        students.append(new_student)
        datasheets.remove(sheet)
        print(name)
        print(len(sheet.courses))

    #Outputs the students
    output_dicts = []
    for student in students:
        for course in student.data_sheet.courses:
            output_dict = {}
            output_dict["stud_name"] = student.name
            output_dict["course_name"] = course.name
            output_dict["teacher"] = course.teacher
            output_dict["gender"] = student.gender
            output_dict["ECTS"] = course.ects
            output_dict["classroom"] = course.classroom
            output_dict["grade"] = course.grade
            output_dict["img_url"] = student.image_url
            output_dicts.append(output_dict)
    
    newline=None
    with open('./outputCSV.csv', 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)
        output_writer.writerow(output_dicts[0].keys())
        for row in output_dicts:
            output_writer.writerow(row.values())



def import_students():
    students = []
    filename = "./outputCSV.csv"
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for row in reader:
            print('Row #' + str(reader.line_num) + ' ' + str(row))
            course = Course(row[1],row[5],row[2],int(row[4]))
            try:
                course.set_grade(int(row[6]))
            except:
                course.set_grade(row[6])
            datasheet = DataSheet()
            tmp_student = Student(row[0],row[3],row[7],datasheet)

            if len(students) > 0:
                #todo if any students
                already_exists = False
                for student in students:
                    if tmp_student.name == student.name:
                        student.data_sheet.add_course(course)
                        already_exists = True
                if(already_exists == False):
                    tmp_student.data_sheet.add_course(course)
                    students.append(tmp_student)
            else:
                #todo for first student
                tmp_student.data_sheet.add_course(course)
                students.append(tmp_student)
        print(len(students))

        
        students.sort(key=lambda x: x.get_avg_grade())
        x_list = []
        y_list = []
        for student in students:
            student.print_my_details()
            x_list.append(student.name)
            y_list.append(student.get_avg_grade())
        
        mpl.use("pdf")
        # reset defaults because we change them further down this notebook
        mpl.rcParams.update(mpl.rcParamsDefault)

        plt.bar(x_list,y_list,width=0.5, align='center')
        plt.xticks(rotation=45, horizontalalignment='right',fontweight='light')

        plt.savefig('./barchart.png', bbox_inches='tight')

        #task for progression of study points
        def calc_studypoint_groups(input_students):
            presentation_dict = {"0-19":0,"20-39":0,"40-59":0,"60-79":0,"80-100":0}
            for i_student in input_students:
                print(i_student.name)
                print(i_student.get_current_progression())
                if 0 <= i_student.get_current_progression() <= 19:
                    presentation_dict["0-19"] += 1
                elif 20 <= i_student.get_current_progression() <= 39:
                    presentation_dict["20-39"] += 1
                elif 40 <= i_student.get_current_progression() <= 59:
                    presentation_dict["40-59"] += 1
                elif 60 <= i_student.get_current_progression() <= 79:
                    presentation_dict["60-79"] += 1
                elif 80 <= i_student.get_current_progression() <= 100:
                    presentation_dict["80-100"] += 1

            plt.figure()
            plt.bar(presentation_dict.keys(),presentation_dict.values(), align='center')

            plt.savefig('./barchart2.png', bbox_inches='tight')


        calc_studypoint_groups(students)
        


random_generator_and_output()
import_students()

iter_courses = iter(datasheet1)

tmpCourse = next(iter_courses)
print(tmpCourse.name)
tmpCourse = next(iter_courses)
print(tmpCourse.name)
tmpCourse = next(iter_courses)
print(tmpCourse.name)

#students.pop()
#students.pop()
#students.pop()

task2_1 = Student.get_3_students_closes_to_done(students)
print("3 closest students is: ")
for student in task2_1:
    print(student.name, student.get_current_progression())
