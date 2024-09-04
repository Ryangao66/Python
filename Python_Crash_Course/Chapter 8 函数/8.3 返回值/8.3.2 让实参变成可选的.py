# Owner: Ryan
# Date: 04-Sep-2024
# 在函数中有不确定的parameter

# 不确定有的放在最后
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name("Ludwig", "Beethoven")
print(musician)
musician = get_formatted_name("wolfgang", "amadeus", "mozart")
print(musician)
