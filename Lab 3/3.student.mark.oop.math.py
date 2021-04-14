student_list = []
course_list = []

class student:
    def __init__(self, stName="", stId="", stDob="", courses=""):
        self.stName   = stName
        self.stId    = stId
        self.stDob    = stDob
        self.courses = courses
    
    def inputSt(self, name, stId, stDob, courses):
        st = student(name, stId, stDob, courses)
        student_list.append(st)
    
    def listSt(self, st):
        print(f'Name: {st.stName}')
        print(f'Id: {st.stId}')
        print(f'Date Of Bird: {st.stDob}')
        for u, v in st.courses.items():
            print(f'Mark for {u}: {v}')
        print('*****************\n')
    
    def listCourse(self, course_name):
        
        anotherStList = []
        
        for i in range(len(student_list)):
            for u, v in student_list[i].courses.items():
                if course_name == u:
                    anotherStList.append(student_list[i].stName)
        
        print(f'number of student in {course_name}: {len(anotherStList)}')
        print('Student list: ')
        for i in anotherStList:
            print(f'             - {i}')
            
    def deleteSt(self, name):
        for i in range(len(student_list)):
            if name == student_list[i].stName:
                print(f'student {name} is deleted')
                del student_list[i]

class course:
    def __init__(self, courseId="", courseName=""):
        self.courseId = courseId
        self.courseName = courseName
    
    def inputCourse(self, courseId, courseName):
        c = course(courseId, courseName)
        course_list.append(c)
    
    def mark(self, name, courseName, mark):
        for i in range(len(student_list)):
            if name in student_list[i].stName:
                student_list[i].courses[courseName] = mark

class GPA:
    def __init__(self, name=''):
        self.namee = name

    def calcGPA(self, name, credit):
        ls = []
        for i in range(len(student_list)):
            if name == student_list[i].stName:
                print(student_list[i].courses)
                ls.append(student_list[i].courses)
                grade = np.array([list(d.values()) for d in ls])
                credit = np.array(credit)
                gpa = grade.dot(credit)/sum(credit)
                return tuple((name, gpa))
    
    def sort(self):
        gpa_list = []
        for i in range(len(student_list)):
            gpa_list.append(self.calcGPA(student_list[i].stName, [3, 5]))
        sorted_list = sorted(gpa_list, key=lambda i: i[1])
        for head,tail in enumerate(sorted_list):
            print(f"Ranking {head+1} is {tail[0]} with {tail[1]} points")


st = student()
st.inputSt('Aiden', 'bi10-124', '2001', {})
st.inputSt('dat', 'bi9-066', '1000', {})
st.inputSt('ngoc anh', 'bi10-010', '2001', {})
m = course('','')
m.inputCourse(0, 'programing with python')

m.mark('Aiden', 'programing with python', 10)
m.mark('ngoc anh', 'programing with python', 20)
m.mark('dat', 'programing with python', 15)

m.mark('Aiden', 'signal', 12.5)
m.mark('ngoc anh', 'signal', 15)
m.mark('dat', 'signal', 17.6)

gpa = GPA()
gpa.sort()
