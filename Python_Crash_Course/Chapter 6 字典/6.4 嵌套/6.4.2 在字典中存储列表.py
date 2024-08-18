# Owner: Ryan
# Date: 18-Aug-2024

""" 格式
name = {
    "aa": "aa",
    "bb": ["bb1", "bb2"]
}
"""

# 存储客户所点披萨的信息
pizza = {
    "crust": "thick",
    "toppings": ["mushrooms", "extra cheese"]
}

# 描述客户锁点的披萨
print(f"you ordered a {pizza["crust"]}-crust pizza " 
      "with the following toppings:")
for topping in pizza["toppings"]:
    print(f"\t{topping}")

"""
过年想吃蒸饺还是煮饺，什么陷的
1. 蒸饺
2. 肉三鲜，猪肉酸菜

dumplings = {"type": "蒸饺",
             "flavors": ["肉三鲜", "猪肉酸菜"]
             }

print(f"今年过年的饺子是{dumplings["type"]},有 ")
for flavor in dumplings["flavors"]:
    print(f"\t{flavor}")
print("两种口味")

"""

