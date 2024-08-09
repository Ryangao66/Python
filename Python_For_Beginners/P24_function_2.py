# Owner: Ryan
# Date: 09-Aug-2024
# 代码DRY原则 (Don't Repeat Yourself)

"""
写一个计算BMI的函数，名为calculate_BMI
1. 可以计算任意体重和身高的BMI
2. 执行过程中打印一句话，"你的BMI分类为：xx"
3. 返回计算出的结果

BMI = 体重 / (身高 ** 2)

偏瘦: user_BMI <= 18.5
正常: 18.5 < user_BMI <= 25
偏胖: 25 < user_BMI <= 30
肥胖: user_BMI > 30
"""

def calculate_BMI(weight, height):
    BMI = weight / (height ** 2)
    if BMI <= 18.5:
        category = "偏瘦"
    elif BMI <= 25:
        category = "正常"
    elif BMI <= 30:
        category = "偏胖"
    else:
        category = "肥胖"
    print(f"你的BMI指数为: {category}")
    return BMI

result = calculate_BMI(84, 185)
print(result)
