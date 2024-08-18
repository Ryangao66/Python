# Owner: Ryan
# Date: 10-Aug-2024

# 用"w" 写文件， "a" 把内容添加到文件
# with open("/Users/ryangao/Downloads/python.txt", "w", encoding="utf-8") as file:
#     file.write("Hello!\n")
#     file.write("Python")

"""
任务1: 在一个新的名字为“poem.txt”的文件里，写入一下内容：
# 我欲乘风归去，
# 又恐琼楼玉宇，
# 高处不胜寒。

任务1: 在上面“poem.txt”的文件结尾处，添加一下两句：
# 起舞弄清影，
# 何时在人间。
"""

with open("/Users/ryangao/PycharmProjects/Python/Python_For_Beginners/poem.txt", "w", encoding="utf-8") as file:
    file.write("我欲乘风归去，\n又恐琼楼玉宇，\n高处不胜寒。\n")

with open("/Users/ryangao/PycharmProjects/Python/Python_For_Beginners/poem.txt", "a", encoding="utf-8") as file:
    file.write("起舞弄清影，\n何时在人间。\n")
