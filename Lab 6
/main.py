from Input import Input
from Oupt import Output
import pickle

class domain:
    def __init__(self):
        pass
    def execute(self):
        st = Input('' ,'', '' ,  0)
        st.inputSt('dat', 'bi9-066', '2000', (('Advanced Programming ','15'), ('French ','17'), ('Singal ','18')))
        st.inputSt('Aiden', 'bi10-124', '2001', (('Advanced Programming ','17.5'),('French ','15.25'), ('Singal ','14.25')) )
        st.inputSt('Na', 'bi10-010', '2001', (('Advanced Programming','16.75'),('French','18.04'), ('Signal', '20')) )
        
        st.writeFile(st.student_list)
        
        st.pickleCompress('students.dat')
        st.pickleDecompress()

if __name__ == "__main__":
    main = domains() 
    main.execute()