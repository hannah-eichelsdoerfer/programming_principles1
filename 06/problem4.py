# Problem: 
# Write a program that 
#   - allows the user to enter the marks of 5 students in 4 courses
#   - and outputs the highest average marks for students and courses. 
# Hint: Consider 2 dimensional lists, i.e. the element of a list is a list.

# Sample Run:
# Student 1 (courses 1-4): 50 60 70 60 
# Student 2 (courses 1-4): 100 90 87 90
# Student 3 (courses 1-4): 70 100 90 90
# Student 4 (courses 1-4): 30 65 50 50
# Student 5 (courses 1-4): 58 50 74 43
# The highest average mark of students: 91.75
# The highest average mark of courses: 74.2

# Linda Inputs:
# list of lists
# students = [ [_, _, _, _],
#              [_, _, _, _],
#              [_, _, _, _],
#              [_, _, _, _] ]

# students[2][1]

# Function to calculate the average of a list of numbers
def get_average(grades):
    return sum(grades) / len(grades)

# Prompt the user to enter the grades for each student
input1 = input("Student 1 (courses 1-4): ").split()
input2 = input("Student 2 (courses 1-4): ").split()
input3 = input("Student 3 (courses 1-4): ").split()
input4 = input("Student 4 (courses 1-4): ").split()
input5 = input("Student 5 (courses 1-4): ").split()

# Convert the input strings to integers (list comprehension)
student1 = [int(x) for x in input1]
student2 = [int(x) for x in input2]
student3 = [int(x) for x in input3]
student4 = [int(x) for x in input4]
student5 = [int(x) for x in input5]

students = [
    student1, 
    student2, 
    student3, 
    student4, 
    student5
    ]

# Calculate the average of each student
highest_avg_students = 0
for grades in students:
    average_stud = get_average(grades)
    if average_stud > highest_avg_students:
        highest_avg_students = average_stud

# Calculate the average of each course
highest_avg_courses = 0
course_grades = list(zip(*students))
for grades in course_grades:
    average_course = get_average(grades)
    if average_course > highest_avg_courses:
        highest_avg_courses = average_course

# Print the highest average marks for students and courses
print(f"The highest average mark of students: {highest_avg_students}")
print(f"The highest average mark of courses: {highest_avg_courses}")

