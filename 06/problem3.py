# Problem: 
# We’ll say that a lowercase ’g’ in a string is ”happy” if there is another ’g’ immediately to its left or right. 
# Write a function to print True if all the g’s in the given string are happy, otherwise, print False.

# isHappy = True

# loop through the string
#   testing chars for gs
#   if single g
#     isHappy = False
#     break the loop

def isHappy(str):
    gcount = str.count("g")
    if gcount == 0:
        return True
    if gcount == 1:
        return False
    if gcount > 1:
        for char in str:
            if char == "g":
                if str[str.index(char) + 1] == "g" or str[str.index(char) - 1] == "g":
                    continue
                else:
                    return False
        return True

word = input("String: ")

print(f"Happy? {isHappy(word)}")