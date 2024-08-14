# Owner: Ryan
# Date: 12-Aug-2024
# 设置变量，根据变量的输入结果取不同结果
# if-elif-else 练习

favorite_fruits = ["avocado", "kiwi fruit", "apple", "pear", "banana"]

fruit = input("What's your favorite fruit?: ")

if fruit in favorite_fruits:
    print(f"You really like {fruit}!")
else:
    print(f"Sorry, {fruit} is not on today's menu!")
    