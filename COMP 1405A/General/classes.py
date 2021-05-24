class Student:
    ''' represents a strudent at CU '''

    #fields
    name = None
    age = None
    id = -1
    courses = []

#    def initStudent(s,name,age,id):
#        s.name = name
#        s.age = age
#        s.id= id

    def __init__(self,name,age,id,course = []):
        self.name = name
        self.age = age
        self.id = id
        self.course = course
    
    def __repr__(self):
        return f'{repr(self.name)}, {repr(self.age)}, {repr(self.course)}'
    
    def __str__(self):
        return f'name is {repr(self.name)}, age {repr(self.age)}, courses{repr(self.course)}'

s1 = Student("cat",14,144)
s2 = Student("DOG", 29, 4, ["comp1405"])
#s1.name = "Matei"
#s1.age = 12
#s1.id = 1
#initStudent(s1, "cat" , 12, 35)
'''
print("Student s1 is:" , s1)
print("Student s1 name is:", s1.name)
print("Student s1 id is:", s1.id)
print("Student s1 courses is:", s1.courses)
print(s2.name, s2.age, s2.id,s2.course)
'''
print(s2)
