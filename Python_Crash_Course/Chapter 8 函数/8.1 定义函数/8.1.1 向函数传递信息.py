# Owner: Ryan
# Date: 29-Aug-2024
# 定义 def greet_user(username):
# 打印 greet_user('username')

# 函数greet_user()括号里有内容的时候
def greet_user(username):
    print(f"Hello, {username.title()}")


# 打印的时候括号里也必须有内容，否则报错
greet_user('jesse')
# 这样报错
# greet_user()
