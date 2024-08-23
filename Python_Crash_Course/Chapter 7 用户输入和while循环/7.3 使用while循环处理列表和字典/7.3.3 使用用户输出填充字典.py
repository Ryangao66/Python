# Owner: Ryan
# Date: 23-Aug-2024
# 1. 询问用户信息，并把信息加入到字典用
# 2. 当flag是False时候，终止while循环
# 3. 用for循环把用户输入信息打印出来

# 设置一个空字典
responses = {}
# 设置一个flag，指出调查是否继续
polling_active = True

while polling_active:
    # 设置字典中的 key = name
    name = input("\nWhat's your name? ")

    # 设置字典中的value = response
    response = input("Which mountain would you like to climb someday?")

    # 把用户输入的答案储存在字典中
    # name = key: response = value
    responses[name] = response

    # 可以打印出来看看现在字典中有什么
    # print(responses)

    # 询问是否有人需要调查
    repeat = input("Would you like to let another person respond? (yes/no): ")

    # 如果没有flag变成False，然后终止循环
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")
