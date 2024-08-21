# Owner: Ryan
# Date: 21-Aug-2024
# 使用break 来停止程序 (break) = (flag = False)

current_number = 0
while current_number < 10:
    current_number += 1
    # 如果可以被2整除，就跳过，所以只打印出奇数
    if current_number % 2 == 0:
        continue

    print(current_number)