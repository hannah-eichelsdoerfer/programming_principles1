# Problem: 
# Given starting and ending years, write a program with a function to calculate the number of days from starting year to ending year inclusive.  
# Hints: Write a function to check leap year. 
# Sample code is in the lecture notes of Section 10: Type Bool and Boolean Expressions. 
# Sample run:
# Year 1? 1980
# Year 2? 2022
# Number of days: 15706

def isLeap(year):
  isLeap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
  return isLeap

startYear = int(input("Year 1? "))
endYear = int(input("Year 2? "))

num_days = 0

list = list(range(startYear, endYear + 1))

print(len(list))

for year in range(startYear, endYear + 1):
    num_days += 366 if isLeap(year) else 365
    # if isLeap(year):
    #    print("LEAP YEAR")
    #    number_of_days += 366
    # else:
    #    number_of_days += 365

print(f"Number of days: {num_days}")
