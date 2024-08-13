"""
# 披萨制造机
1. 询问客人要什么toppings，按q结束
2. 把toppings加入到list
3. 打印出客人需要的toppings
4. 让客人确认，按y确认
5. 如果客人不输入则询问是否确定要plain pizza
"""
required_toppings = []

user_input = input('What topping would you like on your pizza? (Type "q" to exit): ')
while user_input != "q":
    required_toppings.append(user_input)
    print(f"{user_input} has been added on your pizza.")
    user_input = input('What else would you like on your pizza? (Type "q" to exit): ')
else:
    confirm = input(f'The topping you want on your pizza are {required_toppings}! Type "yes" to exit: ' )
if confirm == "yes":
    print("We are cooking your pizza right now!")
else:
    print("Restart the system and try it again.")