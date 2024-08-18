# Owner: Ryan
# Date: 09-Aug-2024
# 代码DRY原则 (Don't Repeat Yourself)
# pypi.org #publish Python packages

# 计算所有人工资的中位数
def median(num_list):
    sorted_list = sorted(num_list)
    n = len(num_list)
    # 如果一共有奇数个数字，取中间那个
    if n % 2 == 1:
        return num_list[n // 2]
    # 如果一共有偶数个数字，取中间两个的平均值
    else:
        return (num_list[n // 2] + num_list[n // 2] / 2)

print(median([69, 124, 333, 45, 97]))

import statistics
print(statistics.mean([69, 124, 333, 45, 97]))

# import 模块的三种方式
# import
import statistics
# 在使用的时候需要加函数名
print(statistics.mean([69, 124, 333, 45, 97]))

# from...import...
# import 特定模块
from statistics import median, mean
# 在使用的时候不需要加函数名
print(median([19, -5, 36]))
print(mean([19, -5, 36]))

# from...import *
# 把所有模块都import
from statistics import *
# 在使用的时候不需要加函数名
print(median([19, -5, 36]))
print(mean([19, -5, 36]))