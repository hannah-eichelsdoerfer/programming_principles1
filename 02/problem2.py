# Ask for number of hours of work per day
hours_per_day = float(input("Number of hours worked per day: "))
# Ask for number of days work per week
days_per_week = float(input("Number of days worked in a week: "))
# Ask for annual salary
annual_salary = float(input("Annual salary: "))
# Calculate hourly wage
hourly_wage = annual_salary / (hours_per_day * days_per_week * 52)
# Print hourly wage
print(f"Hourly wage = ${hourly_wage}")