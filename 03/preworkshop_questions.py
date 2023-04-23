i = 5
x = 3.4
z = i // x
z1 = x // i
z2 =  x % i

print(z, type(z))
print(z1, type(z1))
print(z2, type(z2))





def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for animal, count in animal_dict.items(): 
        # Use a string method to format the required string.
        result += count 
    return result