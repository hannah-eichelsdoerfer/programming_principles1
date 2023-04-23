# Problem: 
# A car dealer earns a base wage of $36.25 per hour up to their normal work week of 37 hours. 
# Only whole hours are counted. 
# If he works more hours than that (overtime) he gets paid at 1.5 times his normal rate for the overtime. 
# If he sells more than 5 cars in a week, he gets a bonus of $200 per car from the 6th car sold. 
# Write a program that 
# - takes as input the number of hours worked
# - the total number of cars sold for the week
# and outputs the car dealer’s total salary for the week.

base_wage = 36.25
overtime_wage = base_wage * 1.5
normal_hours = 37

# 1. Ask user to input the number of hours worked
hours_worked = float(input("How many hours were worked? ")) // 1
# 2. Ask user to input the number of cars sold
cars_sold = int(input("Total number of cars sold for the week? "))

# 3. Calculate the salary for the hours worked that week
if hours_worked > 37:
    base_salary = base_wage * normal_hours
    overtime_salary = (hours_worked - normal_hours) * overtime_wage
    salary = base_salary + overtime_salary
else:
    salary = base_wage * hours_worked

# 4. Calculate the bonus for the cars sold that week
bonus = (cars_sold - 5) * 200 if cars_sold > 5 else 0

# 5. Calculate the total salary 
total_salary = salary + bonus

# 6. Print the total salary
print(f"The salary is {total_salary}")
