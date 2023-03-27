# Problem: 
# A tradie needs to estimate how much concrete is needed for a rectangular-sized car park. 
# Write a program that asks the user for the 
# - length of the park in metres
# - the width of the park in metres
# - and the volume of concrete required in litres per square metre. 
# Calculate and print the total litres of concrete required for the car park.
# For example, the program should look like this when run.

length = float(input("Length of park (m): "))
width = float(input("Width of park (m) "))
volume = float(input("Litres per square metre: "))
total_litres_required = length * width * volume

print(f"Litres required = {total_litres_required}")
