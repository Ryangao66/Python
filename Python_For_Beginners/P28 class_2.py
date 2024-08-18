# Owner: Ryan
# Date: 10-Aug-2024


# class 命名规则首字母大写
class CuteCat:
    # 创造一个类，类可以包含的对象，名字，年龄，颜色
    def __init__(self, cat_name, cat_age, cat_color):
        self.name = cat_name
        self.age = cat_age
        self.color = cat_color

    def speak(self):
        print("喵" * self.age)
    def think(self, content):
        print(f"小猫{cat1.name}在思考{content}...")

cat1 = CuteCat("Jojo", 2, "橙色")
cat1.think("现在去抓沙发还是去撕纸箱")
print(f"小猫{cat1.name}的年龄是{cat1.age}岁，花色是{cat1.color}")

class RomaPlayer:
    def __init__(self, player_name, player_age, player_position):
        self.name = player_name
        self.age = player_age
        self.position = player_position

player1 = RomaPlayer("Totti", 36, "Forward")
player2 = RomaPlayer("De Rossi", 32, "Midfielder")
player3 = RomaPlayer("Juan", 38, "Defender")
print(f"\n今晚第一位登场的球员是今年{player1.age}的{player1.name}，场上位置是一名{player1.position}。")
print(f"接下来出场的球员是今年{player2.age}的{player2.name}，场上位置是一名{player2.position}。")
print(f"最后出场的罗马球员是{player3.age}的{player3.name}，场上位置是一名{player3.position}。")
class MavsPlayer:
    def __init__(self, player_name, player_age, player_position):
        self.name = player_name
        self.age = player_age
        self.position = player_position

player1 = MavsPlayer("Dirk Nowitzki", 41, "Power forward")
player2 = RomaPlayer("Luca Doncic", 22, "Point guard")
player3 = RomaPlayer("Kyrie Irving", 32, "Point guard")
print(f"\n今晚第一位登场的球员是今年{player1.age}的{player1.name}，场上位置是一名{player1.position}。")
print(f"接下来出场的球员是今年{player2.age}的{player2.name}，场上位置是一名{player2.position}。")
print(f"最后出场的小牛球员是球员是{player3.age}的{player3.name}，场上位置是一名{player3.position}。")

"""
定义一个学生类
要求：
1. 属性包括学生姓名，学号，以及语数英三科的成绩
2. 能够设置学生某科目的成绩
3. 能够打印出学生所有科目的成绩
"""
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):
        if course in self.grades:
            self.grades[course] = grade

    def print_grades(self):
        print(f"\n学生{self.name} (学号:{self.id})的成绩为: ")
        for course in self.grades:
            print(f"{course}: {self.grades[course]}分")

garfield = Student("加菲", "2222")
garfield.set_grade("语文", 20)
garfield.set_grade("数学", 18)
garfield.set_grade("英语", 27)
garfield.print_grades()

# garfield.grade = {"语文": 18, "数学": 27, "英语": 53}
# tian = Student("啊t", "3838", "19", "31", "45")
# tian.grade = {"语文": 7, "数学": 19, "英语": 35}
#
# print(f"\n学号为：{garfield.id}的学生,{garfield.name}, 你的成绩为{garfield.grade},明天让你妈来一趟，不像话。")
# print(f"学号为：{tian.id}的学生,{tian.name}, 你的成绩为{tian.grade}，明天让你妈也来学校一趟，太不像话了。")