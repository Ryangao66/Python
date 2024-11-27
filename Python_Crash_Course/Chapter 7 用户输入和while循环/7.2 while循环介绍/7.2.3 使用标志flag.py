# Owner: Ryan
# Date: 21-Aug-2024
# 使用flag 来让程序在False的时候停止

# 格式
"""
# 打印从1开始
current_number = 1
# 一直打印到20
while current_number <= 20:
    print(current_number)
    # 每打印一个+1
    current_number += 1
"""


prompt = "\nTell me something and I'll repeat to you, "
prompt += "\nEnter 'quit' to quit the game: "

# 当flag是True的时候while循环一直提示用户进行输入
flag = True
while flag:
    message = input(prompt)
    # 当用户输入quit的时候，flag变成False的，while停止
    if message == "quit":
        flag = False
    # 不是quit的时候，while循环继续
    else:
        print(message)
