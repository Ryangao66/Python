# Owner: Ryan
# Date: 08-Aug-2024

# Check if a value is in a list:
car_brands = ["Toyota", "Ford", "Honda", "Chevrolet", "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Nissan", "Hyundai"]
brand_to_check = str(input("What car you like the most?: ").title())

if brand_to_check in car_brands:
    print(f"{brand_to_check.title()} is on the list!")
else:
    print(f"{brand_to_check.title()} is not on the list!")

# Check the number is even or odd:
number = int(input("\nPlease input a number: "))

if number % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd")

# Check if a person is eligible to vote (age 18 or older):
age = int(input("\nHi, how old are you?: "))

if age >= 18:
    print("Eligible to vote!")
else:
    print("Not eligible to vote!")

# Check if an item is in either of two lists:
fruits = ["banana", "apple", "kiwi fruit"]
veges = ["carrot", "brocolli", "spinach"]
item_to_check = str(input("\nWhat's your favorite fruit or vegetables: "))

if item_to_check in fruits or veges:
    print(f"{item_to_check.title()} is on tonight's dinner menu!")