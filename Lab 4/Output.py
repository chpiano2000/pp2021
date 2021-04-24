class Output:
    def __init__(self, student_list=''):
        self.student_list = student_list

    def listSt(self, student_list):
        for i in student_list:
            print(f"Name: {i.stName}")
            print(f"Id: {i.stId}")
            print(f"Date Of Birth: {i.stDob}")
            for j in range(len(i.courses)):
                print(f"Marks of {i.courses[j][0]} :", i.courses[j][1])
            print("*************************")