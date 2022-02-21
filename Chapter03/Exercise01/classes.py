class Student():
    def __init__(self,name,gender,image_url,data_sheet):
        self.name = name
        self.gender = gender
        self.image_url = image_url
        self.data_sheet = data_sheet

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        filtered_grades = [grade for grade in grades if isinstance(grade,int)]
        if len(filtered_grades) > 0:
            return int(sum(filtered_grades)/len(filtered_grades))
        else:
            return 0
    
    def print_my_details(self):
        print("Name: ",self.name," Img_url: ",self.image_url," Avg grade: ",self.get_avg_grade())

    def get_current_progression(self):
        total = sum([course.ects for course in self.data_sheet.courses if isinstance(course.grade,int)])
        return round((total/150)*100)
    
    @staticmethod
    def get_3_students_closes_to_done(students):
        if len(students) < 3:
            raise NotEnoughStudentsExceptions('You only gave ',len(students)," students, 3 is minimum")
        students.sort(key=lambda x: x.get_current_progression(), reverse=True)
        sorted_students = students[:3]
        for student in students:
            print(student.name, student.get_current_progression())
        return sorted_students

class DataSheet():
    def __init__(self):
        self.courses = []

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.courses):
            course = self.courses[self.n]
            self.n += 1
            return course
        else:
            raise StopIteration

    def get_grades_as_list(self):
        if self.courses != False:
            outputlist = [course.grade for course in self.courses]
            return outputlist

    def add_course(self,course):
        self.courses.append(course)

    
class Course():
    def __init__(self,name,classroom,teacher,ects):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ects = ects
        self.grade = None

    def set_grade(self,new_grade):
        self.grade = new_grade
    
class NotEnoughStudentsExceptions(Exception):
    pass