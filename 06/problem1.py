# Problem: 
# Write a program that 
#   - reads strings (without digits or symbols in the string) typed by the user 
#   - until an empty string is entered. 
# For each string:
#   - convert all words to lowercase, 
#   - then sort and print the words into descending order lexicographically. 
# Hint: use split function to split a string into a list, then sort it with a method.

user_input = None

while user_input != "": # indefinite loop
    # user_input = input("Enter a input: ").lower()
    # list_of_words = user_input.split()
    # list_of_words.sort(reverse=True)
    user_input = input("Enter a string: ")
    words = user_input.lower().split()
    sorted_words = sorted(words, reverse=True)
    output = " ".join(sorted_words)

    print(f"Output: {output}")