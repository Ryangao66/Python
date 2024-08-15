# Owner: Ryan
# Date: 07-Aug-2024

# 创建一个元组
menu = ("butter chicken", "sweet pork", "garlic beef", "lemon chicken", "fried rice" )
for dish in menu:
    print(dish.title())

# 尝试修改一个元素会报错
# menu[0] = "rice noodle"

# 修改后的菜单
menu_new = ("\nlamb rib", "sweet pork", "steak", "lemon chicken", "fried rice" )
for dish in menu_new:
    print(dish.title())

