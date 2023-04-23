# Problem: 
# A palindrome is a number or a text phrase that reads the same backwards as well as forwards. 
# Examples of palindromes are 123321, 1234321, 55555, 22, 454, 1, 0. 
# Write a program that: 
# - reads in a positive integer number
# - and prints out whether or not that number is a palindrome

# Sample run:
# Enter a positive number: 12321
# 12321 is a palindrome
# Enter a positive number: 1234
# 1234 is not a palindrome

int_input = input("Enter a positive number: ")

reversed = int_input[::-1]

try:
  if int(int_input) == int(reversed):
      print(f"{int_input} is a palindrome")
  else:
      print(f"{int_input} is not a palindrome")
except:
  print("Invalid input")
