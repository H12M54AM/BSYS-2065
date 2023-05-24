"""
Ch 11 Question 2 - Find the Average in student data txt
---
Edward Naidoo
BSYS-2065
May 23, 2023
"""
grades = []
def average(student:list) -> int:
    """Calculates the average of a list of grades"""
    return round(sum(student) / len(student), 2)

with open('./data/studentdata.txt', 'r') as data:
    for i in data:
        items = i.split()
        grades = items[1:]
        int_grades = [int(i) for i in grades]
        print(int_grades)
        print(f"The Avg: {average(int_grades)}")
