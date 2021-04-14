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

for i in range(len(student_list)):
    st.listSt(student_list[i])

st.listCourse('programing with python')

st.deleteSt('ngoc anh')

for i in range(len(student_list)):
    st.listSt(student_list[i])