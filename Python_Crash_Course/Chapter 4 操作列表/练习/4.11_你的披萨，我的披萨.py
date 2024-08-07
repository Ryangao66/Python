# Owner: Ryan
# Date: 07-Aug-2024

# 创建两个变量
my_pizzas = ["pepperoni", "five cheese", "meat lover", "double bacon"]
friend_pizzas = my_pizzas[:]

# 在变量中添加元素
my_pizzas.append("butter chicken")
friend_pizzas.append("bbq")

# 打印两个变量的list
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza.title())
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())


