# Owner: Ryan
# Date: 09-Aug-2024
# 代码DRY原则 (Don't Repeat Yourself)

# 求扇形面积 - 作为被定义的函数
# central_angele = 160
# radius = 30
# sector_area = central_angele / 360 * 3.14 * radius ** 2
# print(f"此扇形铭记为{sector_area}")

def calculate_sector(central_angle, radius):
    sector_area = central_angle / 360 * 3.14 * radius ** 2
    print(f"此扇形铭记为{sector_area}")

calculate_sector(160, 30)
...
calculate_sector(60,15)
...
calculate_sector(30, 16)
