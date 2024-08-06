# Owner: Ryan
# Date: 06-Aug-2024

numbers = list(range(1,6))
print(numbers)

# 从2开始，然后不断加2，直到11
even_numbers = list(range(2, 11, 2))
print(even_numbers)

# 创建一个空列表
squares = []
# 从1-10
for value in range(1, 11):
    # 计算1的平方，到10的平方
    square = value ** 2
    # 把1的平方，到10的平方加入到空的列表中
    squares.append(square)

print(squares)


# 更简洁写法
squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

# extra
print(min(squares))
print(max(squares))
print(sum(squares))
