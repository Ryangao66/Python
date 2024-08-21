# Owner: Ryan
# Date: 20-Aug-2024
# % 只显示余数是多少，不是显示结果

print(4 % 3)
print(5 % 3)
print(6 % 3)
print(7 % 3)

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")
