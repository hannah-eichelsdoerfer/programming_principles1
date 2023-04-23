# Problem: 
# A shipping company charges its customer based on the weight of goods and the distance of shipping. 
# A discount is given based on the distance of shipping as follows:
# - distance < 250km, no discount 
# - 250km ≤ distance < 500km, 10% discount
# - 500km ≤ distance < 1000km, 15% discount
# - 1000km ≤ distance < 2000km, 20% discount
# - 2000km ≤ distance < 3000km, 35% discount
# - 3000km ≤ distance, 50% discount
# The shipping cost is calculated based on the following equation: 
# cost = baseprice * weight * distance * (1 - discount).
# Write a program that takes as inputs the baseprice, weight, and distance, and prints the shipping cost to be charged to the customer.

# get values from user input
baseprice = float(input("How much is the base price? "))
weight = float(input("What is the weight? "))
distance = float(input("What is the distance? "))

# determine discount
if distance < 250:
    discount = 0
elif distance < 500:
    discount = 0.1
elif distance < 1000:
    discount = 0.15
elif distance < 2000:
    discount = 0.2
elif distance < 3000:
    discount = 0.35
elif distance >= 3000:
    discount = 0.5


# calculate shipping_cost
shipping_cost =  baseprice * weight * distance * (1 - discount)

# print shipping cost
print(f"The shipping cost is {shipping_cost:.2f}") # round up to 2 decimal places as price is in dollars