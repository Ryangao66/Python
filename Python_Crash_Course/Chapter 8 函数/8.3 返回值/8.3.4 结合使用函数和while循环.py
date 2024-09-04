# Owner: Ryan
# Date: 04-Sep-2024
# 在函数中返回字典

def get_formatted_name(first_name, last_name):
    # 规范化格式名
    full_name = f"{first_name} {last_name}"
    return full_name.title()


# 这是一个无线循环
while True:
    print("\nPlease tell me what's your name: ")
    print("(Enter 'q' to quit!)")
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name,l_name)
    print(f"Hello, {formatted_name}")