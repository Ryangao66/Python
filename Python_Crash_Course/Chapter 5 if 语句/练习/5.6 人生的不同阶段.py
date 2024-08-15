# Owner: Ryan
# Date: 12-Aug-2024
# 设置变量，根据变量的输入结果取不同结果
# if-elif-else 练习

age = int(input("请输入要查询的年龄： "))

if age < 2:
    print("It's fucking baby!")
elif age < 4:
    print("It's a fucking child!")
elif age < 13:
    print("It's a fucking kid!")
elif age < 18:
    print("It's a fucking annoying teens!")
elif age < 65:
    print("It's a miserable adult!")
else:
    print("It's elderly!")

