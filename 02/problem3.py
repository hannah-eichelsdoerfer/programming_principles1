# Problem:
# Each school class has 25 students.
# A big exam hall can accommodate 45 students, and a small exam hall can accommodate 22 students.
# Write a program for the school to calculate how many full classes can be accommodated given the input numbers of big exam halls and small exam halls.

num_students_per_class = 25
big_hall_capacity = 45
small_hall_capacity = 22

num_big_halls = int(input("How many big exam halls? "))
num_small_halls = int(input("How many small exam halls? "))

big_halls_capacity = big_hall_capacity * num_big_halls
small_halls_capacity = small_hall_capacity * num_small_halls

total_capacity = small_halls_capacity + big_halls_capacity

num_full_classes = total_capacity // num_students_per_class  # use // for floor division

print(f"Number of classes = {num_full_classes}".format(num_full_classes))