# Owner: Ryan
# Date: 21-Aug-2024
# 基本的while循环格式

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

message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
