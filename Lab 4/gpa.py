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