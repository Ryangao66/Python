# Owner: Ryan
# Date: 19-Aug-2024

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

favorite_language = {"jen": ["python", "rust"],
                     "sarah": ["c"],
                     "edward": ["rust", "go"],
                     "phil": ["python", "haskell"]
                     }

# 把字典中的key和value单独取出来
for name, languages in favorite_language.items():
    # 先调用单独的key
    print(f"{name.title()}'s favorite languages are: ")
    # 在用for loop 调用在list中的value
    for language in languages:
        print(f"\t{language.title()}")

