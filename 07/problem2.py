# Problem: 
# Write a program that 
# - prompts for the name of a file, 
# - then prints the first two lines and the last two lines of the file.

# Example:
# File name: yesterday.txt
# Output:
# Yesterday Once More 
# When I was young
# I would sing to then
# And I’d memorize each...

# Get file name from user
file_name = input("File name: ")

# Open file
file = open(file_name)

# Read file into list
list = file.readlines()

# Print first two lines
for line in list[:2]:
    print(line, end ='')

# Print last two lines
for line in list[-2:]:
    print(line, end ='')

# print newline to avoid % at the end of the output
print(end = '\n')


# Close file 
file.close()

# print(list)
# print(file.read())

# for line in file:
#     print(line)


