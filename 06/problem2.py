# Problem: 
# Write a program that 
#   - allows the user to enter two lists of integers, 
#   - calculate the sum of the first and the last integers in each list, 
#   - and print the larger sum. 
#   (In the event of a tie, print Same)
# When there is only one integer in the list, the sum is the integer itself.

# Sample Runs:
# List 1: 1 2 3 4 5
# List 2: 5 6 7
# Output: 12
# List 1: 4 3 10 1
# List 2: 9
# Output: 9
# List 1: 4 3 2 1
# List 2: 1 2 3 4
# Output: Same

# 1. ask user for numbers two times
list1 = input("List 1: ").split()
list2 = input("List 2: ").split()

# 2. convert the input strings to integers (list comprehension)
int_list1 = [int(x) for x in list1]
int_list2 = [int(x) for x in list2]

# 3. calculate the sum of the first and the last integers in each list
sum1 = int_list1[0] + int_list1[-1] if len(int_list1) > 1 else int_list1[0]
sum2 = int_list2[0] + int_list2[-1] if len(int_list2) > 1 else int_list2[0]

# 4. print the larger sum
print("Output: Same") if sum1 == sum2 else print(f"Output: {max(sum1, sum2)}")

# Code
# list1 = input("List 1: ").split()
# list2 = input("List 2: ").split()

# int_list1 = list(map(int, list1))
# int_list2 = list(map(int, list2))

# if len(int_list1) == 1:
#     sum1 = int_list1[0]
# else:
#     sum1 = int_list1[0] + int_list1[-1]

# if len(int_list2) == 1:
#     sum2 = int_list2[0]
# else:
#     sum2 = int_list2[0] + int_list2[-1]

# if sum1 == sum2:
#     print("Output: Same")
# else:
#     print(f"Output: {max(sum1, sum2)}")

## Other ways to do it:
# 1. 
# list1 = list(map(int, input("List 1: ").split()))
# list2 = list(map(int, input("List 2: ").split()))
# 2. 
# int_list1 = [int(x) for x in input("List 1: ").split()]
# int_list2 = [int(x) for x in input("List 2: ").split()]

