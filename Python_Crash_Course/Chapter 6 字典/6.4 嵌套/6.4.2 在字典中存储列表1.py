# Owner: Ryan
# Date: 18-Aug-2024

pizza = {
    "crust": "thick",
    "toppings": ["mushroom", "extra cheese"]
}

print(f"You ordered a {pizza["crust"]}-crust pizza with the following toppings: ")
for topping in pizza["toppings"]:
    print(f"\t{topping}")