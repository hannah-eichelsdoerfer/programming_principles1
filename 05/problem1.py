# Problem: 
# Write a program that prompts for and reads strings until a string that starts with the letter “A” is entered (inclusive),
# then prints the longest string that was entered. 

string = ""
longest_string = ""

while not string.startswith("A"):
    string = input("Enter a string: ")

    if len(string) > len(longest_string):
        longest_string = string

print(f"Longest was: '{longest_string}'")

# longest_string = max(longest_string, string, key=len)

# longest_string = ""
# while True:
#     string = input("Enter a string: ")
#     if string.startswith("A"):
#         break
#     if len(string) > len(longest_string):
#         longest_string = string

# print(f"Longest was: '{longest_string}'")

          
