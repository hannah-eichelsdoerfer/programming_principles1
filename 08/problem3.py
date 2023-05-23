# Problem: 
# Write a program with a function that 
# given a list of numbers, returns True if and only if all of the numbers in the list form an arithmetic progression, that is the difference between any two successive numbers in the list is the same. 
# Your main program should read a file containing space-separated numbers as test lists, print each list and the outcome after calling the function.

# Examples:
# File name: numbers.txt
# [1 2 3 4] True
# [10 20 30 40] True
# [10 9 8 7] True
# [2 7 8 3] False
# [1 2 3 5] False

# Define a function that checks if the list of numbers is an arithmetic progression
def is_arithmetic_progression(numbers):
    if len(numbers) == 1:
        return True
    else: 
      difference = numbers[1] - numbers[0]
      for i in range(2, len(numbers)):
          if numbers[i] - numbers[i-1] != difference:
              return False
      return True
    
def main():
    # Ask the user to input a file name
    filename = input("File name: ")
    # Open the file for reading
    with open(filename, 'r') as file:
        # Read each line in the file
        for line in file:
            numbers = list(map(int, line.strip().split()))
            result = is_arithmetic_progression(numbers)
            print(numbers, result)

main()