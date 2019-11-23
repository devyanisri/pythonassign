import os.path
file="C:\\Users\\dsrivastav23\\Documents\\Trainingpy\\Modules\\Assignment"
for i in os.listdir(file):
    print(os.path.splitext(i))
    if os.path.splitext(i)[1] == ".txt":
        fo=open(file+'\\'+i,'r')
        for line in fo:
            print(line)