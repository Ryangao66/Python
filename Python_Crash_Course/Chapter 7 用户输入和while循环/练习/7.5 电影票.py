# Owner: Ryan
# Date: 22-Aug-2024
# 用三种写法练习while loop

# 7.2.2 写法，在while循环中使用条件来终止循环
user_input = "\nFor different age we charge differently, how old are you?"
user_input += "\nType 'quit' when you are finished: "

age = input(user_input)
while age == 'quit':
#    break

    age = int(age)
    if age < 3:
        print("The ticket for age under 3 is free.")
    elif age < 12:
        print("The ticket for age under 12 is $10. ")
    else:
        print("The ticket for age over 12 is $15. ")

"""
# 7.2.3 写法，用flag来终止循环

user_input = "\nFor different age we charge differently, how old are you"
user_input += "\nType 'quit' when you are finished: "

flag = True
while flag:
    age = str(input(user_input))
    if age == 'quit':
        break

    age = int(age)
    if age < 3:
        print("The ticket for age under 3 is free.")
    elif age < 12:
        print("The ticket for age under 12 is $10. ")
    else:
        print("The ticket for age over 12 is $15. ")
        
"""

"""
# 7.2.4写法，用break来终止循环
user_input = "\nFor different age we charge differently, how old are you"
user_input += "\nType 'quit' when you are finished: "

while True:
    # age = 字符串，用户输入quit的时候可以退出
    age = input(user_input)
    if age == 'quit':
        break
    # age = int，用户输入数字的时候可以给结果
    age = int(age)
    if age < 3:
        print("The ticket for age under 3 is free.")
    elif age < 12:
        print("The ticket for age under 12 is $10. ")
    else:
        print("The ticket for age over 12 is $15. ")

"""

