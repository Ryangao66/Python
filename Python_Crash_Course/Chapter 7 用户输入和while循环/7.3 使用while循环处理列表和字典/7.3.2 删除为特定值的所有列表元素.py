# Owner: Ryan
# Date: 23-Aug-2024
# 用while loop 从列表里删除元素

# 创建一个包含许多相同元素的列表
pets = ["dot", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)

while 'cat' in pets:
    pets.remove("cat")
    print(pets)
