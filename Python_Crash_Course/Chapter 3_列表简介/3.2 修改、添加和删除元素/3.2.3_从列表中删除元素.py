# 创建一个列表[], 然后删除列表里面的元素
# 1. del 删除 [0], [1]
# 2. pop 删除 - 默认最后一个
# Owner: Ryan
# Date: 04-Aug-2024

motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

# del motorcycles[0]
# print(motorcycles)
# del motorcycles[1]
# print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)  # pop 出[-1]，只剩下 [0], [1]
print(popped_motorcycles)  # 从list中pop 出来最后一个元素[-1]

last_owned = popped_motorcycles
print(f"The last motorcycle I owned was a {last_owned.title()}!")

motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles)
too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"\n{too_expensive.title()} is too expensive for me!")
