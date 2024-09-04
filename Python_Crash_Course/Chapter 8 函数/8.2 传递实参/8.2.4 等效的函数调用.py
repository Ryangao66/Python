# Owner: Ryan
# Date: 04-Sep-2024
# 给形参指定默认值

def describe_pet(animal_name, animal_type='dog'):
    # 显示宠物信息
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name.title()}")


# 一只名为Willie的小狗
describe_pet("Willie")

# 一只名为Harry的仓鼠
# 只有在调用的时候添加参数，就会优先调用，从而覆盖默认参数
describe_pet("Harry", "Hamster")

