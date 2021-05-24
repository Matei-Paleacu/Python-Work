print("Hello Welcome to Grade Calculator")
name = input("Please enter your name: ")
name = name.capitalize()
finalGrade = None
component1 = None 
component2 = None
assignmentGrade = float(input(name + " ,please enter your assignment grade: "))
tutorialGrade = float(input(name + " ,please enter your tutorial grade: "))
studygroupGrade =float(input(name + " ,please enter your study group grade: "))
midtermGrade = float(input(name + " ,please enter your midterm grade: "))
examGrade = float(input(name + " ,please enter your exam grade: "))

finalAssignmentGrade = assignmentGrade*0.42
finalTutorialGrade = tutorialGrade*0.08
finalStudygroupGrade = studygroupGrade*0.05
finalMidtermGrade = midtermGrade*0.2
finalExamGrade = examGrade*0.25

component1 = finalAssignmentGrade + finalTutorialGrade
component2 = finalMidtermGrade + finalExamGrade

if component1 < 25 and component2 < 22.5:
    if component1 < component2:
        finalGrade = component1
        print(name + "'s final grade is " + str(finalGrade))
        exit()
    else:
        finalGrade = component2
        print(name + "'s final grade is " + str(finalGrade))
        exit()
else : 
    if component1 < 25:
        finalGrade = component1
        print(name + "'s final grade is " + str(finalGrade))
        exit()
    else :
        if component2 < 22.5:
            finalGrade = component2
            print(name + "'s final grade is " + str(finalGrade))
            exit()
        else :
            finalGrade = finalAssignmentGrade + finalTutorialGrade + finalStudygroupGrade + finalMidtermGrade + finalExamGrade
            print(name + "'s final grade is " + str(finalGrade))
            exit()
# Code is writen by Matei Paleacu ID:101187396