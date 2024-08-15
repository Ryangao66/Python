# Owner: Ryan
# Date: 15-Aug-2024

"""
# 把字典加入到列表中
alien_0 = {"color": "green", "point": "5"}
alien_1 = {"color": "yellow", "point": "10"}
alien_2 = {"color": "red", "point": "15"}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

"""

# 自动生成30个外星人

# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色外星人
for alien_number in range(30):
    # 给外星人加上属性
    new_alien = {"color": "green", "point": "5", "speed": "slow"}
    # 把外星人加入到空的aliens列表
    aliens.append(new_alien)


# 显示前5个绿色外星人
for alien in aliens[:5]:
    print(alien)

# 显示一共有多少个外星人
print(f"Total number of aliens: {len(aliens)}")
print("\n")

# 将前3个外星人修改为黄色、速度中、10分
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["point"] = 10

# 显示前5个绿色外星人
for alien in aliens[:5]:
    print(alien)

# 将前4-10个外星人修改为红色、速度高、15分
for alien in aliens[3:10]:
    if alien["color"] == "green":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["point"] = 15

# 打印出所有的外星人
for alien in aliens:
    print(alien)
