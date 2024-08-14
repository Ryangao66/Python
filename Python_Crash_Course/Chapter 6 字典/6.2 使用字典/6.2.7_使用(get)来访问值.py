# Owner: Ryan
# Date: 14-Aug-2024

# dict = {"aa": "bb", "cc": "dd"}
# 键值对  {"key"： "value"}

# get  取值格式
# dict.get("key")

alien_0 = {"color": "green", "speed": "slow"}
print(alien_0)
# "point" 不存在，系统会报错
# print(alien_0["point"])

# 使用get来取字典中的元素
point_value = alien_0.get("point", "No point value assigned")
print(point_value)

# 用get来取不确定是否存在字典中的size值， 返回None，表示size不在字典中
size_value = alien_0.get("size")
# print(size_value)
print(alien_0.get("size"))