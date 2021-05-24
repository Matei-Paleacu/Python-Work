#class Students:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age
#
 #   def __repr__(self):
 #       return f'{repr(self.name)}, {repr(self.age)}'
#    
#    def __str__(self):
#        return f'name is {repr(self.name)}, age{repr(self.age)}'
'''
dog = ["food",6,8]
cat = ["apple",10,14]

dog.append(cat)
print(dog)

for x in range(len(dog)):
    print(dog[x])
    if str(dog[x]).isnumeric() == True:
        
        print("hi")
    else:
        print("no")

hi = dog[1:]
print(hi)
'''
name = "matei"
print(f'hello {6} apple {name}')

def findAverage(courseName,term,studentList):
    avg = 0
    a = 0
    for student in studentList:
        name = student[0]
        id4 = student[1]
        print(name,id4)
        for x in range(len(student)):
            if str(student[x]) == courseName:
                if str(student[x+1]) == term:
                    avg = avg + student[x+2]
                    a+=1
    if avg > 0:
        print(a)
        avg= avg/a
    else:
        avg = -1
    print(name,id4,avg)
    fileOut = open("output.csv", "w")
    fileOut.write(name +","+ str(id4) +","+str(avg)+"\n")

students = [["dog",17,"comp1405","f20",99],["cat",29,"comp1405","f20",45],["turtule",34,"comp1405","f20",78,"comp1805","f21",90]]

print(findAverage("comp1405","f20",students))
'''
list_of_tuples = [("matei",18),("jhon",84),("lucas",8)]

list_of_studetns = list()
#for index, tuple in enumerate(list_of_tuples):
#    list_of_studetns.append(tuple[index])

#print(enumerate(list_of_tuples))
res = [list(ele) for ele in list_of_tuples]         # makse tuple into list
print(res)
res = [tuple(ele) for ele in list_of_tuples]        # makse lsit into tuple+
print(res)
c_l_t = list()
for x in res:
    x = tuple(x)
    c_l_t.append(x)
    print(x)
print(c_l_t)
#res = tuple(res)
#print(res)
#res[0][1] = 5
#print(res)

#for person in res:
#    person[0]=1
#    print(res)
#    res.remove(person)
#print(res)
#res.remove(res[2])
#print(res)
'''
'''
import csv
matei = [[1],[2],[3]]
file = open('studentOut.csv',"w+",newline="")
with file:
    write = csv.writer(file)
    write.writecolumns(matei)
'''
#fileOut = open("student.csv", "w")
#fileOut.write("Matei, 17, comp1405, f20, 90, coomp1805, f20, 95\n" "Lucas, 16, math1007, f19, 87\n" "Marian, 23")

def load_student(filename):
    student = [] 
    with open(filename, "r") as f:
        for line in f:
            student.append( [str(val) for val in line.strip().split(",")] )

    return student
'''

filename = input("enter file name")         #student.csv
print(load_student(filename))

'''
def convertToAverage (inputFile):
    student_list = []
    output_list = []
    studentID = None
    classes = None
    try:         
        student_list = load_student(inputFile)
    except:
        return False
    try:
        for student in student_list:
            if len(student) < 3:
                output_list.append(student)
            else:
                studentID = student[:2]
                classes = student[2:]
                numClass = 0
                avg = 0
                for x in range(len(classes)):
                    if classes[x].strip().isnumeric() == True:
                        avg = avg + int(classes[x].strip())
                        numClass +=1
                studentID.append(avg/numClass)
                output_list.append(studentID)
        import csv
        file = open('studentOut.csv',"w+",newline="")
        with file:
            write = csv.writer(file)
            write.writerows(output_list)
        return output_list
    except:
        return False

filename = input("enter file name")         #student.csv
print(convertToAverage(filename))







