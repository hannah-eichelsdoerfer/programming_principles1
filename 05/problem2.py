# Problem: 
# Write a program with a function that converts all numerical digits in a string to underline.

# string = string.replace(char, "_")

def convert_to_underline(string):
  '''
  Converts all numerical digits in a string to underline

  Parameters:
    string: The string to be converted
  Returns:
    outputs: The converted string
  '''
  output = ""
  for char in string:
    output += "_" if char.isdigit() else char
    
  return output

user_input = input("Input a string? ")

print(convert_to_underline(user_input))

    