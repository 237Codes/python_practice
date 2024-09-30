'''

Write a function calculate_gpa() that calculates the grade point average (GPA) 
for a student based on their course grades and returns the gpa as a float.
The function takes in a dictionary report_card as a parameter where each 
key-value pair represents a course and the grade received in that course respectively. 
The grades are represented as strings ("A", "B", "C", "D", "F") and each grade corresponds 
to a certain number of grade points:

"A" = 4
"B" = 3
"C" = 2
"D" = 1
"F" = 0

'''

'''

UPI - Understand

- Given a dictionary report_card calculate the gpa for a student based on their course grades
- gpa is calculated by finding the average of all grade points
-  return the gpa as a float    

UPI - Plan

- grade mapping to know what grade has what number of points
- get the grade for each course
- get the corresponding mapping for that grade
- add the point to toal points 
- after all points are added, calculate the average of all points

UPI - Impliment

'''
def calculate_gpa(report_card):
    grade_points = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0
    }
    total_points = 0

    for course in report_card:
        total_points += grade_points[report_card[course]]
    gpa = total_points / len(report_card)
    return gpa


report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))