# Problem: 
# In mathematics, the Fibonacci sequence is defined such that:
# each Fibonacci number is the sum of the two preceding ones, starting from 0 and 1. 
# That is, F1 = 0, F2 = 1, F3 = 1, F4 = 2, ..., Fn = F(n-1) + F(n-2). 
# Write a program that given an input n, outputs the first n Fibonacci numbers. 
# The format of output is that at most 4 numbers can be displayed in a row. 

# Sample run:
# Enter a positive number: 6
# 0 1 1 2 
# 3 5
# Enter a positive number: 10
# 0 1 1 2
# 3 5 8 13
# 21 34

# Ask the user for a positive number
n = int(input("Enter a positive number: "))

# Initialize first two Fibonacci numbers
f1, f2 = 0, 1

# Print the first two numbers
print(f"{f1} {f2}", end=" ")

# Print the rest of the numbers
for i in range(2, n):
    # Calculate the next Fibonacci number
    f3 = f1 + f2
    # Print next Fibonacci number
    print(f"{f3}", end=" ")
    # Shift the numbers over
    f1 = f2
    f2 = f3
    # If we have outputted 4 numbers, print newline
    if i % 4 == 3:
        print()

# If n is not a multiple of 4, print a newline (to avoid the % at the end of the output)
if n % 4 != 0:
    print()

# Final Version:
# Get a positive number from the user
# num = int(input("Enter a positive number: "))

# # Initialize the first two Fibonacci numbers
# f1, f2 = 0, 1

# if num >= 1:
#     print(f"{f1}", end=" ")
# if num >= 2:
#     print(f"{f2}", end=" ")
# if num == 1:
#     print(f"{f1}", end=" ")
# elif num == 2:
#     print(f"{f1} {f2}", end=" ")
# else:
#     print(f"{f1} {f2}", end=" ")
#     for i in range(3, num + 1):
#         f3 = f1 + f2
#         print(f"{f3}", end=" ")
#         f1 = f2
#         f2 = f3
#         if i % 4 == 0:
#             print()

# Version 2: 
# n = int(input("Enter a positive number: "))

# f1, f2 = 0, 1

# for i in range(n):
#     print(f1, end=" ")
#     f1, f2 = f2, f1 + f2
#     if (i + 1) % 4 == 0:
#         print()

# if n % 4 != 0:
#     print()

# # Print the first two numbers
# print(f"{f1} {f2}", end=" ")

# # Print the rest of the numbers
# for i in range(2, num):
#     # Calculate the next Fibonacci number
#     f3 = f1 + f2
#     # Print the next Fibonacci number
#     print(f"{f3}", end=" ")
#     # Shift the numbers over
#     f1 = f2
#     f2 = f3
#     # If we have printed 4 numbers, print a newline
#     if i % 4 == 3:
#         print()
