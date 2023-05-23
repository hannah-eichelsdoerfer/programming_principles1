# Problem: 
# Write a program that 
#   - prompts for the name of a file containing numbers in each line, 
#   - prints the average of each line. 
# Assume each line contains numbers only and they are separated by spaces.

# File name: scores.txt
# The average of line 1 is 60.0
# The average of line 2 is 91.75
# The average of line 3 is 48.75
# The average of line 4 is 56.25

# file_name = input("File name: ")
# file = open(file_name)

# for i, line in enumerate(file):
#     numbers = [int(num) for num in line.split()]
#     average = sum(numbers) / len(numbers)
#     print(f"The average of line {i + 1} is {average}")

# file.close()

# Ask user for file name
file_name = input("File name: ")

# Open file
with open(file_name) as file:
    lines = file.readlines()

# Loop through each line
for i, line in enumerate(lines):
    numbers = [int(num) for num in line.split()]
    average = sum(numbers) / len(numbers)
    print(f"The average of line {i+1} is {average}")

# file.close() not needed as the with statement automatically takes care of closing the file when you're done with it

