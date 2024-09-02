# Owner: Ryan
# Date: 02-Sep-2024
# 给形参指定默认值

def describe_pet(animal_name, animal_type='dog'):
    # 显示宠物信息
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}")


# 宠物类型已经默认是dog，所有不需要在提供
describe_pet("Willie")