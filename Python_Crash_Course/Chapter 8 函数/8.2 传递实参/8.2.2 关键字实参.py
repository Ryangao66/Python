# Owner: Ryan
# Date: 29-Aug-2024

def describe_pet(animal_type, animal_name):
    # 显示宠物信息
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {animal_name}.")


describe_pet(animal_type="labrador", animal_name="Hazel")
# 把函数中的parameter直接加入，可以随意变换位置
describe_pet(animal_name="willie", animal_type="dog")
