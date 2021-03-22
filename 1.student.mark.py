student_list = []
course_list = []

def info():
    stNum = input("Number of student ")
    for i in range(int(stNum)):
        stId = input("Student id ")
        stName = input("Student name ")
        stDob = input("Student dob ")
        student_list.append({'Student name': stName, 'Student id': stId, 'Student DOB': stDob})
        
    courseNum = input("Number of course ")
    for i in range(int(courseNum)):
        courseId = input("Course id ")
        courseName = input("Course name ")
        course_list.append({'Course name': courseName, 'Course id': courseId})

def add_grad():
    for i in student_list:
        print("for student {} ".format(i['Student name']))
        for j in course_list:
            i[j['Course name']] = input("Mark for {} course ".format(j['Course name']))

def listing():
    print("List of students: ")
    for i in student_list:
        print('- {}'.format(i['Student name']))

    print("\n")
    print("List of courses: ")
    for i in course_list:
        print('- {}'.format(i['Course name']), end=' ')
        
    print("\n")
    print("Mark for a given courses: ")
    for i in student_list:
        print(" ")
        print("- {}: ".format(i['Student name']))
        for j in course_list:
            print('    + {}'.format(j['Course name']), end=": ")
            print('{} point'.format(i[j['Course name']]))

info()
add_grad()
listing()