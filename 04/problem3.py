# Problem: Given an input number n, print a diamond shape with 2*n-1 rows.

# Sample run:
# Enter a positive number: 3 
#   x
#  xxx
# xxxxx
#  xxx
#   x

n = int(input("Enter a positive number: "))

empty_space = " "
shape = "x"


for i in range(0, n):
    print(empty_space * (n-i-1) + shape * (2*i+1))

for i in range(n-2, -1, -1):
    print(empty_space * (n-i-1) + shape * (2*i+1))


    
    






    