"""
Ch 7 Question 3 - Student Grades
---
Edward Naidoo
BSYS-2065
April 11, 2023
"""
user = float(input("What is your grade?: "))

def getGrade(userGrade):
    if userGrade >= 90:
        return "A"
    elif userGrade >= 80 and userGrade < 90:
        return "B"
    elif userGrade >= 70 and userGrade < 80:
        return "C"
    elif userGrade >= 60 and userGrade < 70:
        return "D"
    elif userGrade < 60 and not userGrade < 0:
        return "F"
    else:
        return "W h a t . . . ?"

print(getGrade(user))