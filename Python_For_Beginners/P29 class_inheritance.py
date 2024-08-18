# Owner: Ryan
# Date: 10-Aug-2024

"""
class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.num_eyes = 2

    def breath(self):
        print(self.name + "在呼吸...")

    def poop(self):
        print(self.name + "在拉屎...")

class Human(Mammal):
    def read(self):
        print(self.name + "在阅读...")

class Cat(Mammal):
    def scratch_sofa(self):
        print(self.name + "在抓沙发...")


# 把内容添加到parent class
# human1 = Mammal("Peter", "Male")
# print(f"{human1.name} 是sb")

# 把内容添加到child class
human1 = Human("Peter", "Male")
print(human1.breath())

"""

"""
类继承练习：人力资源
- 员工分为两类：全职员工 FullTimeEmployee、兼职员工PartTimeEmployee
- 全职和简直都有"姓名 name"、"工号 id"属性
- 都具有 "打印信息 print_info" (姓名、工号)方法
- 全职有"月薪 monthly_salary"属性
- 简直有"日薪 daily_salary"属性、"每月工作天数 work_days"的属性
- 全职和简直都有"计算月薪 calculate_monthly_pay"的方法，但具体计算过程不一样
"""

"""
一下是我写的垃圾，以后在来补充
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class FullTimeEmployee(Employee):
    def monthly_salar(self):
        print(f"{self.name} 这个月的工资是 ")

class PartTimeEmployee(Employee):
    def daily_salary(self):
        print(f"{self.name} 这个月的工资是 ")

    def work_days(self):
        print(f"{self.name}这个月工作的天数是 ")

alice = Employee("alice", 95070)
print(f"员工名字：{alice.name}, 员工工号{alice.id}")


"""


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print_info(self):
        print(f"员工名字: {self.name}, 员工工号: {self.id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, id, daily_salary, work_days):
        super().__init__(name, id)
        self.daily_salar = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salar * self.work_days


alice = FullTimeEmployee("alice", "95070", 6000)
anu = PartTimeEmployee("anu", "60013", 230, 15)
alice.print_info()
anu.print_info()
print(alice.calculate_monthly_pay())
print(anu.calculate_monthly_pay())
