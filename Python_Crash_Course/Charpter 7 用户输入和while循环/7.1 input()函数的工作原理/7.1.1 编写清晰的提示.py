# Owner: Ryan
# Date: 20-Aug-2024
# 使用input进行简单的用户输入

# name = input("Please enter your name: ")
# (f"Hello, {name}")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat's your first name? "

name = input(prompt)
print(f"\nHello, {name}!")
