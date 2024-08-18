# Owner: Ryan
# Date: 09-Aug-2024


# class 命名规则首字母大写
class CuteCat:
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

cat1 = CuteCat("Jojo", 2, "橙色")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")



"""
类继承练习：人力资源
- 员工分为两类：全职员工 FullTimeEmployee、兼职员工PartTimeEmployee
- 全职和简直都有"姓名 name"、"工号 id"属性
- 都具有 "打印信息 print_info" (姓名、工号)方法
- 全职有"月薪 monthly_salary"属性
- 简直有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性
- 全职和简直都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样
"""