# Owner: Ryan
# Date: 05-Sep-2024
# 定义一个函数，然后调用列表中的元素并且打印出来

# 定义一个打招呼的函数
def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


# 把所有需要打招呼的名字储存在列表中
usernames = ["hannah", "ty", "Margot"]
# 调用函数，打招呼
greet_users(usernames)