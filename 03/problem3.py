# Problem: 
# Write a program that takes as input 3 integers and outputs them in descending order.

input1 = int(input("Integer 1? "))
input2 = int(input("Integer 2? "))
input3 = int(input("Integer 3? "))

input_numbers = [input1, input2, input3] # sorted_integers = sorted([input1, input2, input3], reverse=True)
input_numbers.sort(reverse=True)

print(f"Sorted: {input_numbers}")

# integers = []
# integers.append(int(input("Integer 1? ")))
# integers.append(int(input("Integer 2? ")))
# integers.append(int(input("Integer 3? ")))
# integers.sort(reverse=True)
# print(integers)
