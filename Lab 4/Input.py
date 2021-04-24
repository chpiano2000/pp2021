class Input:
    def __init__(self, stName="", stId="", stDob="", courses=""):
        self.stName   = stName
        self.stId    = stId
        self.stDob    = stDob
        self.courses = courses
        self.student_list = []

    def inputSt(self, name, stId, stDob, courses):
        st = Input(name, stId, stDob, courses)
        self.student_list.append(st)

    def deleteSt(self, name):
        for i in range(len(self.student_list)):
            if name == self.student_list[i].stName:
                print(f'student {name} is deleted')
                del self.student_list[i]