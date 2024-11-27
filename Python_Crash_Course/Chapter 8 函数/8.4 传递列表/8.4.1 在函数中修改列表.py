# Owner: Ryan
# Date: 05-Sep-2024


# 首先创建一个列表，其中包含要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，知道没有未打印的设计为止
# 打印每个设计后，都将其移动到completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following modes have been printed: ")
for completed_model in completed_models:
    print(f"\t{completed_model}")


# 用定义函数写法

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []


def print_models(unprinted_designs, completed_models):
    # 模拟打印每个设计，知道没有未打印的设计为止
    # 打印每个设计后，都将其移动到completed_models中
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing design: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # 显示所有打印好的模型
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

"""
更容易理解的写法
unprinted = ['phone case', 'robot pendant', 'dodecahedron']
completed = []


def print_models(unprinted, completed):
    while unprinted:
        current = unprinted.pop()
        print(f"Printing design: {current}")
        completed.append(current)


def show_completed_models(completed):
    print("\nThe following models have been printed: ")
    for model in completed:
        print(model)

"""