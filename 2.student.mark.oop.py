class Student:
    def __init__(self):
        self._id = ""
        self._name = ""
        self._dob = ""
        self._marks = {}
    
    def input_info(self):
        self._id = input("Enter student ID: ")
        self._name = input("Enter student name: ")
        self._dob = input("Enter student date of birth (DD/MM/YYYY): ")
    
    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_dob(self):
        return self._dob
    def set_mark(self, course_name, mark):
        self._marks[course_name] = mark
        
class Course:
    def __init__(self):
        self.id = ""
        self.name = ""

    def input_info(self):
        self.id = input("Enter course ID: ")
        self.name = input("Enter course name: ")
    
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    
classroom = []
courses_list = []
num_students = int(input("Enter number of students: "))
for i in range(num_students):
    student = Student()
    student.input_info()
    classroom.append(student)

num_courses = int(input("Enter number of courses: "))
for i in range(num_courses):
    course = Course()
    course.input_info()
    courses_list.append(course)

for course in courses_list:
    print(f"Course: {course.get_name()}")
    print(f"Course ID: {course.get_id()}")

while True:
    selected_course_id = input("Enter the ID of course that you want to add mark (Type 'exit' to stop): ")
    if selected_course_id == "exit": 
        break 
    else:
        for s in classroom:
            print(f"Student: {s.get_name()} - ID: {s.get_id()}")
            mark = float(input("Enter the mark: "))
            s.set_mark(selected_course_id, mark)
