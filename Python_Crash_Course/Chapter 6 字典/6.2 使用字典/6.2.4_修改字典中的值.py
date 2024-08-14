# Owner: Ryan
# Date: 14-Aug-2024

# dict = {"aa": "bb", "cc": "dd"}
# 键值对  {"key"： "value"}
# 修改元素速度、坐标

alien_0 = {}
print(alien_0)

# 分别加入str,int到字典中
alien_0["color"] = "green"
alien_0["point"] = 5
print(f"The alien is {alien_0["color"]}")

# 把颜色换成yellow
alien_0["color"] = "yellow"
# 使用{dict}["key"]来从字典中调用元素
print(f"The alien is now {alien_0["color"]}.")

# 看外星人如何移动
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print(f"Original position: {alien_0["x_position"]}")

# 修改alien的速度
alien_0["speed"] = "fast"

# 向右移动外星人
# 根据当前速度决定外星人移动多远
if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # 这个外星人移动速度肯定很快
    x_increment = 3
# 新位置 = 旧位置 + 移动速度
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0["x_position"]}")
