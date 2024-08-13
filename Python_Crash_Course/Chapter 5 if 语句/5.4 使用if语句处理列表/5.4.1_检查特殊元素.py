# Owner: Ryan
# Date: 13-Aug-2024

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
toppings = input("What toppings would you like?: ")

for toppings in requested_toppings:
    if toppings == "green peppers":
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {toppings}.")

print("\nFinished making your pizza.")
