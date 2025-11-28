students = []   
courses = []    
marks = {}      

def input_students():
    n = int(input("Enter number of students: "))

    for i in range(n):
        print(f"\n--- Student {i+1} ---")
        sid = input("ID: ")
        name = input("Name: ")
        dob = input("Date of Birth: ")

        students.append({
            "id": sid,
            "name": name,
            "dob": dob
        })


def input_courses():
    n = int(input("\nEnter number of courses: "))

    for i in range(n):
        print(f"\n--- Course {i+1} ---")
        cid = input("Course ID: ")
        name = input("Course name: ")
        
        courses.append({
            "id": cid,
            "name": name
        })


def enter_marks():
    print("\n--- Courses ---")
    for i, c in enumerate(courses):
        print(f"{i+1}. {c['id']} - {c['name']}")

    cindex = int(input("Select a course index to enter marks: ")) - 1

    print(f"\nEntering marks for course: {courses[cindex]['name']}")

    for i, s in enumerate(students):
        mark = float(input(f"Enter mark for {s['name']}: "))
        marks[(i, cindex)] = mark


def list_students():
    print("\n--- Student List ---")
    for s in students:
        print(f"{s['id']} - {s['name']} - {s['dob']}")


def list_courses():
    print("\n--- Course List ---")
    for c in courses:
        print(f"{c['id']} - {c['name']}")


def show_marks_for_course():
    print("\n--- Courses ---")
    for i, c in enumerate(courses):
        print(f"{i+1}. {c['id']} - {c['name']}")

    cindex = int(input("Select a course index to show marks: ")) - 1

    print(f"\n--- Marks for Course: {courses[cindex]['name']} ---")
    for i, s in enumerate(students):
        mark = marks.get((i, cindex), None)
        if mark is not None:
            print(f"{s['name']}: {mark}")
        else:
            print(f"{s['name']}: No mark entered")


input_students()
input_courses()
enter_marks()

print("\n")
list_students()
list_courses()
show_marks_for_course()


