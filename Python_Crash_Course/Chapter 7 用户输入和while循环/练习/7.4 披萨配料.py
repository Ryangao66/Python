# Owner: Ryan
# Date: 22-Aug-2024
# 用三种写法练习while loop

# 7.2.2 写法，在while循环中使用条件来终止循环
user_input = "\nWhat kind of topping would you like, "
user_input += "type 'quit' when you are finished: "

selected_toppings = []
message = ""

while message != "quit":
    message = input(user_input)
    if message != "quit":
        print(f"{message.title()} has been added onto your pizza.")
        selected_toppings.append(message.title())


print(f"\nWe have added {selected_toppings} onto your pizza.\nThank you for your order. "
      f"Cooking your pizza now!!! ")



# 7.2.3 写法，用flag来终止循环
user_input = "\nWhat kind of topping would you like, "
user_input += "type 'quit' when you are finished: "
selected_toppings = []

flag = True
while flag:
    message = input(user_input)
    if message == 'quit':
        flag = False
    else:
        print(f"{message.title()} has been added onto your pizza.")
        selected_toppings.append(message.title())
        
print(f"\nWe have added {selected_toppings} onto your pizza.\nThank you for your order. "
      f"Cooking your pizza now!!! ")

"""
# 7.2.4写法，用break来终止循环
user_input = "\nWhat kind of topping would you like, "
user_input += "type 'quit' when you are finished: "
selected_toppings = []

while True:
    toppings = input(user_input)

    if toppings == 'quit':
        break
    else:
        print(f"{toppings.title()} has been added onto your pizza.")
        selected_toppings.append(toppings)

print(f"\nWe have added {selected_toppings} onto your pizza.\nThank you for your order. "
      f"Cooking your pizza now!!! ")
"""