# temperature_list = [36.4, 36.6, 41.5, 38.1, 39.2, 36.7, 36.6, 39.2]
# for temperature in temperature_list:
#     if temperature >= 38:
#         print(temperature)
#         print("完球了，明天别来了")

temp_dict = {"啊猫": 37.5,
             "啊狗": 38.9,
             "啊鸡": 39.5,
             "啊鸭": 40.1,
             "啊牛": 45.6,
             "啊猪": 36.7,
             "啊花": 36.5,
             "啊啊": 37.2,
             }

temp_dict.keys()  # 所有键
temp_dict.values()  # 所有值
temp_dict.items()  # 所有键值对

for staff_id, temp in temp_dict.items():
    if temp >= 38:
        print(staff_id)

for i in range(5, 10):
    print(i)

for o in range(1, 10, 2):
    print(o)

total = 0
for i in range(1,101):
    total = total + i
print(total)
