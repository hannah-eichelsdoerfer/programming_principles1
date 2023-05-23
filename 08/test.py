vowels = ["a", "e", "i", "o", "u"]

# 4. function to find names starting with vowel
def names_starting_with_vowels(names):
    names_starting_with_vowels = []
    # loop over all names
    for name in names:
        # find first letter of name
        first_letter_of_name = name[0].lower
        # check if first letter is a vowel
        if first_letter_of_name in vowels:
            # if so add to list with names I want to return
            names_starting_with_vowels.append(name)
    # return all names starting with vowels
    return names_starting_with_vowels

def names_starting_with_vowels1(names):
    names = []
    for vowel in vowels:
        for name in names:
            if name.startswith(vowel):
                names.append(name)
    
    return names

        

# 1. Ask for input
names = input("Names: ")

# 2. turn input into list
names_list = names.split()

# 3. call function with names_list
test = names_starting_with_vowels1(names_list)
print(test)