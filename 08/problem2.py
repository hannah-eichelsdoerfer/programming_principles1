# Problem:
# Given two lists, write a program with a function that takes these two lists as the input arguments 
# and returns the list of all the elements in the first list that occur in the second list. 
# The returned list shall not contain duplicate elements. 
# Your main program will allow the user to enter two lists of numbers and end the program by inputting a blank line for list 1.

# List 1: 1 3 3 6
# List 2: 3 4 2 1 2 1 3
# Output: [1, 3]
# List 1: 3 4 2 1 2 1 3
# List 2: 5 6 7 8
# Output: [] 

# List 1:

# Ask the user to input two list of numbers while the user does not input a blank line for list 1
blank_line = False

def ask_user_for_input():
  
  return integer_list1, integer_list2

# Define function that finds common elements in the two lists
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

while not blank_line:
  input_list1 = input("List 1: ")
  if input_list1 == "":
    blank_line = True
    break;
  input_list2 = input("List 2: ")
  # convert the input list of numbers into a list of integers
  integer_list1 = [int(x) for x in input_list1.split()]
  integer_list2 = [int(x) for x in input_list2.split()]
  # print the common elements in the two lists
  print(f"Output: {find_common_elements(integer_list1, integer_list2)}")

  










