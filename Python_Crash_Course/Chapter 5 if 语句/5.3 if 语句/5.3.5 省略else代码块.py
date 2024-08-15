# Owner: Ryan
# Date: 12-Aug-2024

age = int(input("How old are you?: "))

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
    # 65岁以上半价
elif age >= 65:
    price = 20
# 可以没用else

print(f"Your admission cost is ${price}")
