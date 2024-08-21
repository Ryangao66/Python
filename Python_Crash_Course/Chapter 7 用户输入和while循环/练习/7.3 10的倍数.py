# Owner: Ryan
# Date: 21-Aug-2024

number = int(input("请输入数字，我会告诉你是不是10的倍数： "))
if number % 10 == 0:
    print(f"你输入的数字{number}是10的倍数。")
else:
    print(f"你输入的数字{number}不是10的倍数。")