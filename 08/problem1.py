# Problem: 
# Write a program with a function that 
# given a list of numbers, rotate the numbers so the first number becomes the last, and the rest of the numbers move one position forward. 
# Do the rotation iteratively until the list of numbers returns to its initial form.
# Input a list: 1 2 3 4
# [1, 2, 3, 4]
# [2, 3, 4, 1]
# [3, 4, 1, 2]
# [4, 1, 2, 3]
# [1, 2, 3, 4]

# Ask the user to input a list of numbers
input_list = input("Input a list: ")

# convert the input list of numbers into a list of integers
integer_list = [int(x) for x in input_list.split()]

# Define a function to rotate the list by one position to the left
def rotate(num_list):
    num_list.append(num_list[0])
    num_list.pop(0)
    return num_list 

# print the input list of numbers
print(integer_list)

# rotate the list of numbers until it returns to its initial form
for i in range(len(integer_list)):
    print(rotate(integer_list)) # the rotate() function modifies the actual input_list in place

    
    


