# Owner: Ryan
# Date: 13-Aug-2024

# Format for this practice
"""
for:
    if:
        print
    else:
        print

print
"""
available_toppings = ["mushrooms", "olives", "green pepper", "pepperoni", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza.")
