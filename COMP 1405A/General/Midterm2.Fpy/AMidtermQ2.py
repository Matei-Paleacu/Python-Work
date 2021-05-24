# Midterm 2
# Question 2


#  contents for sample input file
'''
cat, 81.1
dog, 17.2
eel, 51.3
owl, 83.4
cow, 68.1
rat, 56.9
ram, 71.3
'''
# expected output file (as calculated with MS Excel using these numbers; your result might be slightly different)
'''
7, 61.3285714
owl, 83.4
'''

#fileOut = open("grades.csv", "w")
#fileOut.write("cat, 81.1\n" "dog, 17.2\n" "eel, 51.3\n" "owl, 83.4\n" "cow, 68.1\n" "rat, 56.9\n" "ram, 71.3\n")

def load_student(filename):
    student = [] 
    with open(filename, "r") as f:
        for line in f:
            student.append( [str(val) for val in line.strip().split(",")] )

    return student





def data2stats(inFile, outFile):    
    try:      
        student_list = load_student(inFile)  #grades.csv
        number_of_names = 0
        average_grade = 0
        max_grade = 0
        max_name = ""
        for student in student_list:
            number_of_names +=1
            average_grade = average_grade + float(student[1].strip())
            if float(student[1].strip()) > max_grade:
                max_grade = float(student[1].strip())
                max_name = student[0]
        fileOut = open(outFile, "w")                        #gradesOut.csv
        fileOut.write(str(number_of_names) +"," + str(average_grade/number_of_names) + "\n" + str(max_name) + "," + str(max_grade) + "\n")
        return True
    except:
        return False

inp = input("Please enter inputfile")
out = input("Please enter outputfile")
print(data2stats(inp,out))

