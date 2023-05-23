# Problem: 
# The Unix tool wc counts the numbers of characters, words and lines in a file. 
# Write your own version of wc that prompts for the name of the file to read, then prints the counts. 
#   - Assume a word may contain letters, digits, symbols and their mixture, but not space. 
#   - Hyphenated words, e.g. large-scale, shall be considered as one word.

# Example:
# File name: python.txt
# Characters: 1227
# Words: 176
# Lines: 10

# Code:

# Get file name from user
filename = input("File name: ")

# Open file and read text
with open(filename, 'r', encoding='utf-8') as file: #  When opening a file using the with statement, Python automatically takes care of closing the file when you are done with it.
    text = file.read()
    char_count = len(text)
    word_count = len(text.split())
    line_count = text.count('\n') + 1  # Add 1 for last line which might not have newline character

    # Print output
    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Lines: {line_count}")


# Version 2:

# # Get file name from user
# file_name = input("File name: ")

# # Open file
# file = open(file_name, "r")

# # Initialize variables
# characters = 0
# words = 0
# lines = 0

# # Loop through each line in file
# for line in file:
#     # Increment lines
#     lines += 1

#     # Split line into words
#     line_words = line.split()

#     # Loop through each word in line
#     for word in line_words:
#         # Increment words
#         words += 1

#         # Increment characters
#         characters += len(word)

# # Close file
# file.close()

# # Print results (using f-strings)
# print(f"Characters: {characters}")
# print(f"Words: {words}")
# print(f"Lines: {lines}")



