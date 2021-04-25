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
    
    def compress(self, nameFile):
        list_files = ['students.txt','courses.txt','marks.txt']
        
        compression = zipfile.ZIP_DEFLATED
        z = zipfile.ZipFile(nameFile, mode="w")
        
        for file in list_files:
            z.write(file, file, compress_type=compression)
        z.close()
        
    def decompress(self):
        try: 
            with zipfile.ZipFile("students.dat","r") as zip_ref:
                    zip_ref.extractall("decompress")
        except Exeption as e:
            print('students.dat not found')
            print('error :',e)
    
    def writeFile(self, st):
        for i in st:
            with open("students.txt", "a+") as f1:
                f1.write("Name: "+i.stName+'\n')
                f1.write('Id: '+i.stId+'\n')
                f1.write('Date of birth: '+i.stDob+'\n')

            with open('courses.txt','a+') as f2:
                f2.write('Name :'+i.stName+'\n')
                for j in i.courses:
                    f2.write('Course:'+j[0]+'\n')

            with open('marks.txt','a+') as f3:
                f3.write('Name :'+i.stName+'\n')
                for j in i.courses:
                    f3.write(f'{j[0]}:'+j[1]+'\n')
        f1.close()
        f2.close()
        f3.close()
                    
    def deleteSt(self, name):
        for i in range(len(self.student_list)):
            if name == self.student_list[i].stName:
                print(f'student {name} is deleted')
                del self.student_list[i]