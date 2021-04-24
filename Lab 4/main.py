from Student import student
from Courses import Courses
from gpa import GPA

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
