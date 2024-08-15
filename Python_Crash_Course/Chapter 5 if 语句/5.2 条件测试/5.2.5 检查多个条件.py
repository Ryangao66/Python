# Owner: Ryan
# Date: 08-Aug-2024

# 用and连接两个条件，有一个不过就是False
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

# 用and连接两个条件，只有都通过是True
age_0 = 22
age_1 = 23
# 容易阅读写法
print((age_0 >= 21) and (age_1 >= 21))

# 用or连接两个条件，有一个通过就是True
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

# 用or连接两个条件，只有都不通过的时候是False
age_0 = 17
print(age_0 >= 21 or age_1 >= 21)

# 简写一行检查两个条件
a = 2
b = 5
print("YES") if a == b else print("NO")
