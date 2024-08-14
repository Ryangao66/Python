#
# for loop: 有明确循环对象或次数
# while loop: 循环次数未知
#

list1 = ["你", "好", "吗", "兄", "弟"]
for x in list1:
    print(x)

print(("============"))

for x in range(len(list1)):
    print(list1[x])

print(("============"))

i = 0

while i < len(list1):
    print(list1[i])
    i = i + 1
print(("============"))

for i in range(5, 10):
    print(i)
print(("============"))

# https://youtu.be/moAHW5PEHM8?list=PL5y2P1AqpsZ-79NNUImnYdCHH5jwoyzSa&t=116

# 平均值计算器
# 用户可以输入任意数字，输入q表示输入完成，程序给出平均值结果

print("哈喽呀！我是一个求平均值的计算器")
total = 0
count = 0
user_input = input("请输入数字, 输入q结束: ")
while user_input != "q":
    num = float(user_input)
    total += num  # total = total + num
    count += 1  # count = count + 1
    user_input = input("请再次输入(1-10), 输入q结束: ")
#   print("请再次输入(1-10), 输入q结束: ")  # 用print为什么会无限循环，而user_input不会
if count == 0:
    result = 0
else:
    result = total / count
print("您输入的数字平均值为" + str(result))

#     x = x + 1
# while x == str("q"):
#     print("游戏结束，你的结果是")


# 用while打印str
list = ["joey", "chandler", "ross",]
list.insert(0, "monica")
list.append("Phoebe")
list.append("Rachael")

name = 0
while name < len(list):
    print(list[name].upper())
    name = name + 1  # name += 1


# Stop the loop if i is 3.

i = 1
while i < 6:
    if i ==3:
        break
    i += 1

# In the loop, when i is 3, jump directly to the next iteration.

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)