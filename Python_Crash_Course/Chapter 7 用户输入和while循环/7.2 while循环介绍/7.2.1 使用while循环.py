# Owner: Ryan
# Date: 21-Aug-2024

# 格式


print("\n正常打印1-20")
# 打印从1开始
current_number = 1
# 一直打印到20
while current_number <= 20:
    print(current_number)
    # 每打印一个+1
    current_number += 1

print("\n正常打印0-9")
x = 0
while x < 10:
    print(x)
    x += 1

print("\n正常打印0-9，到5的时候终止")
x = 0
while x < 10:
    print(x)
    if x == 5:
        break
    # x += 1 需要在break后面
    x += 1

print("\n正常打印0-9，到5的时候跳过")
x = 0
while x < 10:
    # x += 1 需要在continue前面
    x += 1
    if x == 5:
        continue
    print(x)

print("\n正常打印0-9，到5的时候跳过")
x = 0
while x < 6:
    print(x)
    x += 1
else:
    print("x is no longer less than 6")