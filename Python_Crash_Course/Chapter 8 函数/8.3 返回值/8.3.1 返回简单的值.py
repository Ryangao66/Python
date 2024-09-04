# Owner: Ryan
# Date: 04-Sep-2024
# 返回简单的值

def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("jimi", "hendrix")
print(musician)
