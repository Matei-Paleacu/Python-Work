# Midterm 2
# Question 3

# sample dictionaries
comp1405 = { -1:['comp1405',-1], 1:['cat', 98.1], 2:['dog', 50], 3:['eel', 82], 4:['owl', 65.2] }
comp1805 = { -1:['comp1805',-1], 1:['cat', 0], 2:['dog', 77], 3:['eel', 90],4:['owl', 0], 5:['elk', 87] }

print(comp1405[1][1])

def betterStudents(d1,d2):
    course_1 = d1[-1]
    course_1 = course_1[0]
    course_2 = d2[-1]
    course_2 = course_2[0]
    d1_big = 0
    d2_big = 0
    for key in d1:
        for key2 in d2:
            if key > 1 or key == 1:
                if key2 == key: 
                    if d1[key][1] > d2[key][1]:
                        d1_big += 1
                    else:
                        d2_big +=1
    if d1_big > d2_big:
        return course_1
    if d2_big > d1_big:
        return course_2
    else:
        return "equal"


print(betterStudents(comp1405,comp1805))