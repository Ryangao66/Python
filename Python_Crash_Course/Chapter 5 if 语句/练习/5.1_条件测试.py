# Owner: Ryan
# Date: 08-Aug-2024

brands = ["Toyota", "Ford", "Honda", "Chevrolet", "BMW", "Mercedes-Benz", "Audi", "Volkswagen", "Nissan", "Hyundai"]

# test 1
car = "Audi"
if car in brands:
    print(f"{car.title()} is on our shopping list!")
else:
    print(f"\n{car.title()} is not on our shopping list!")

# test 2
car = "BMW"
if car in brands:
    print(f"\n{car.title()} is on our shopping list!")
else:
    print(f"\n{car.title()} is not on our shopping list!")

# test 3
car = "Toyota"
if car in brands:
    print(f"\n{car.title()} is on our shopping list!")
else:
    print(f"\n{car.title()} is not on our shopping list!")

# test 4
car = "Honda"
if car in brands:
    print(f"\n{car.title()} is on our shopping list!")
else:
    print(f"\n{car.title()} is not on our shopping list!")

# test 5
car = "Benz"
if car in brands:
    print(f"\n{car.title()} is on our shopping list!")
else:
    print(f"\n{car.title()} is not on our shopping list!")

# test 6
car = "Aston Martin"
if car not in brands:
    print(f"\nSorry, We can't afford {car.title()}!")

# test 7
car = "Mercedes"
if car not in brands:
    print(f"\nSorry, We can't afford {car.title()}!")

# test 8
car = "McLaren"
if car not in brands:
    print(f"\nSorry, We can't afford {car.title()}!")

# test 9
car = "Ferrari"
if car not in brands:
    print(f"\nSorry, We can't afford {car.title()}!")

# test 10
car = "Prius"
if car not in brands:
    print(f"\nSorry, We can't afford {car.title()}!")
