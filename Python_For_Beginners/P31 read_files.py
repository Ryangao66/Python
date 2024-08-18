# Owner: Ryan
# Date: 10-Aug-2024

# r = read only, w = write
file = open("/Users/ryangao/Downloads/python.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()

# 打开文件的另一种方式
with open("/Users/ryangao/Downloads/python.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        print(line)

# 只读一行
# print(file.readline())
# 读所有行
# print(file.readlines())
