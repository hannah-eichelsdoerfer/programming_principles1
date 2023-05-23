# Problem: 
# Given two lists, write a program with a function that merges these two lists in descending order. 
# Your main program will allow the user to enter two lists of numbers and end the program by inputting a blank line for list 1. 
# You are not allowed to concatenate the two lists into a new list and then call the built-in sort() function to sort the new list in descending order. 
# But you are allowed to sort the two lists in descending order before merge. 
# Don’t worry about the complexity of the merging algorithm.

# List 1: 1 3 3 6
# List 2: 1 4 5
# [6, 5, 4, 3, 3, 1, 1] 
# List 1: 100
# List 2: 1 1 3
# [100, 3, 1, 1] 

# Define a function that merges two lists in descending order
def merge_lists_descending(list1, list2):
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    merged_list = []
    while list1 and list2:
        if list1[0] > list2[0]:
            merged_list.append(list1[0])
            list1.pop(0)
        else:
            merged_list.append(list2[0])
            list2.pop(0)
    if list1:
        merged_list.extend(list1)
    if list2:
        merged_list.extend(list2)
    return merged_list

def main():
    # Ask the user to input two list of numbers while the user does not input a blank line for list 1
    stop = False

    while not stop:
        list1 = input("List 1: ")
        if list1 == "":
            stop = True
            break;
        list2 = input("List 2: ")
        # convert the input list of numbers into a list of integers
        list1 = [int(num) for num in list1.split()]
        list2 = [int(num) for num in list2.split()]
        print(merge_lists_descending(list1, list2))

main()


