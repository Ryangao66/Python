# Owner: Ryan
# Date: 11-Aug-2024
# LAMBDA 匿名函数，一次性函数，在代码中可能只使用一次


def calculate_and_print(num, calculator, formatter):
    result = calculator(num)
    formatter(num, result)


def print_with_vertical_bar(num, result):
    print(f"""
    | 数字参数 | {num} |
    | 计算结果 | {result} |""")


def calculate_square(num):
    return num * num


def calculate_cube(num):
    return num * num * num


def calculate_plus_10(num):
    return num + 10


def calculate_time_5(num):
    return num * 5


calculate_and_print(3, calculate_square, print_with_vertical_bar)
calculate_and_print(7, calculate_plus_10, print_with_vertical_bar)

"""
# lambda 函数 写法
lambda num1, num2: num1 + num2


def calculate_sum(num1, num2):
    return num1 + num2

以上两种写法都一样    
"""
# lambda 的使用
calculate_and_print(5, lambda num: num * 10, print_with_vertical_bar)
