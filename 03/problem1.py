# Problem: 
# The grades at a university are awarded based on the marks awarded for the course out of 100. 
# Marks of 85 or above receive the grade of 7.
# Marks less than 85 but that are 75 or above receive the grade of 6.
# Marks less than 75 but that are 65 or above receive the grade of 5. 
# Marks less than 65 but that are 50 or above receive the grade of 4. 
# Anything less than 50 gets the grade of F. 
# Write a program that asks the user to input the marks and prints the grade awarded.

# 1. Ask user to input the mark points
marks = float(input("How many marks? "))

# 2. Logically transform the mark points to the respective GPA grade
if marks >= 85:
    grade = "7"
elif marks >= 75:
    grade = "6"
elif marks >= 65:
    grade = "5"
elif marks >= 50:
    grade = "4"
else:
    grade = "F"

# 3. Print the awarded grade
print(f"Grade awarded: {grade}")
