# Owner: Ryan
# Date: 20-Aug-2024
# 使用int把str变成int

age = input("How old are you? ")
print(age)

"""
age = int(age)
if age >= 18:
    print(True)
else:
    print(False)
"""

height = input("How tall you are, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou are tall enough to ride.")
else:
    print("\nYou'll be able to ride when you're a little order.")
