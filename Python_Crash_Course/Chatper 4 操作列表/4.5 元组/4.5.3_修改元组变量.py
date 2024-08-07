# Owner: Ryan
# Date: 07-Aug-2024
# 元组(tuple)
# 元组(a, b)，不可修改 - 用[0]打印
# 列表[a, b], 可以修改 - 用[0]打印

# 定义元组
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# 重新定义元组来修改元组内容
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)