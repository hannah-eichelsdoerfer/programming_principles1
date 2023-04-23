# Problem: 
# Write a program that reads whole numbers typed by the user until a zero is entered, 
# then prints the number of positive numbers that were entered. 

# Sample run:
# Enter a number: 3
# Enter a number: -2
# Enter a number: 5
# Enter a number: 6
# Enter a number: -100
# Enter a number: 70
# Enter a number: 22
# Enter a number: 68
# Enter a number: 0 
# 6 positive numbers were entered.

count_positive_nums = 0
number = None

while number != 0:
    # Get a number from the user
    number = int(input("Enter a number: "))
    # If the number is positive, increment the count
    if number > 0:
        count_positive_nums += 1

print(f"{count_positive_nums} positive numbers were entered.")

