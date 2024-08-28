# Owner: Ryan
# Date: 21-Aug-2024
# 使用break 来停止程序 (break) = (flag = False)


prompt = "\nTell me something and I'll repeat to you, "
prompt += "\nEnter 'quit' to quit the game: "

"""
flag = True
while flag:
    msg = input(prompt)
    if msg == "quit":
        flag = False
    else:
        print(msg)
"""

""" # 我的写法
prompt = "Please enter the name of a city you have visited,"
prompt += "\nEnter 'quit' when you are finished: "
visited_city = []

flag = True
while flag:
    message = input(prompt)
    
    if message == "quit":
        break
    else:
        print(message.title())
        visited_city.append(message.title())

print(f"You have visited {visited_city} before.")
"""

prompt = "Please enter the name of a city you have visited,"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    city = input(prompt)

    if city == "quit":
        break
    else:
        print(f"I'd like to go to {city.title()}!")
