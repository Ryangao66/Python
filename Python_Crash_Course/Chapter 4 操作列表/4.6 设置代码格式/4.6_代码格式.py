# Owner: Ryan
# Date: 07-Aug-2024
# Python 增强提案 (Python Enhancement Proposal, PEP)
# 锁进4个空格，建议使用tab来锁进
# 行长不要超过80个，最好控制在72个以内，PEP8 标准
# https://peps.python.org/pep-0008/

# 代码格式要保持一直
# 先写注释,下面是内容
tuple = (0, 1, 5, 10, 15, 20)
for num in tuple:
    print(num)

# 上一段写完之后空一行
# 在写下面的注释
print("\n")
juniper_url = 'https://www.juniper.com'
print(juniper_url.removeprefix('https://'))
print(juniper_url.removesuffix('.com'))

# Correct:

# income = (grass_wages
#           + taxable_interest
#           + (dividends - qualified_dividends)
#           - ira_deduction
#           - student_loan_interest)

# Correct:

# Aligned with opening delimiter.
# foo = long_function_name(var_one, var_two,
#                          var_three, var_four)

# Add 4 spaces (an extra level of indentation) to distinguish arguments from the rest.
# def long_function_name(
#         var_one, var_two, var_three,
#         var_four):
#     print(var_one)

# Hanging indents should add a level.
# foo = long_function_name(
#     var_one, var_two,
#     var_three, var_four)
