"""
                   数据类型
｜---------｜-----｜-------------｜
 “Hello”     “呦”     字符串 str
  6          -32      整数  int
  6.0        10.07    浮点数 float
  True       False    布尔类型 bool
     None             空值 NoneType

"""

print(type("hello"))
print(type(6))
print(type(6.05))
print("\n")
print(type(True))
print(type(None))


print(len("Hello"))

# 对字符串求长度
s = "Hello World!"
print(len(s))

# 通过索引获取单个字符W
print(s[6])
print(s[11])
print(s[len(s) - 3])

# 布尔类型

a1 = True
b1 = False


# 空值类型
n = None

# type函数
print(type(s))
print(type(a1))
print(type(b1))
print(type(n))
print(type(1.5))




