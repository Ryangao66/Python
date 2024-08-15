# Owner: Ryan
# Date: 11-Aug-2024


age = int(input("How old are you?: "))
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is {price}")
