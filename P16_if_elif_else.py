# 格式
#
# if [条件一]:
#     if  [条件二]:
#         [语句A]
#     else:
#         [语句B]
#

# mood_index = int(input("今天心情怎么样?: (1-100)"))
# is_at_home = True
#
# if mood_index < 60:
#     if is_at_home:
#         print("放弃游戏，低调做人")
#     else:
#         print("自由！")

# 偏瘦: user_BMI <= 18.5
# 正常: 18.5 < user_BMI <= 25
# 偏胖: 25 < user_BMI <= 30
# 肥胖: user_BMI > 30

user_weight = float(input("请输入你的体重（单位：kg）?: ")) # float 可以算83.5kg
user_height = float(input("请输入你的身高（单位：m）?: "))
user_BMI = int(user_weight / user_height ** 2)
user_sex = str(input("请输入你的性别（男/女）?: "))
if user_BMI <= 18.5:
    if user_sex == str("男"):
        print("先生你好，你的BMI是 " + str(user_BMI) + ",有些偏瘦，天太热吃不下去饭啊")
    # if user_sex == str("女"):
    else:
        print("女士你好，你的BMI是 " + str(user_BMI) + ",有些偏瘦，但是非常完美")
elif 18.5 < user_BMI <= 25:
    if user_sex == str("男"):
        print("先生你好，你的BMI是 " + str(user_BMI) + " ,体重正常，一看就是肌肉猛男")
    # if user_sex == str("女"):
    else:
        print("女士你好，你的BMI是 " + str(user_BMI) + ",体重正常，前凸后翘")
elif 15 < user_BMI <= 30:
    if user_sex == str("男"):
        print("先生你好，你的BMI是 " + str(user_BMI) + ",体重偏胖，少吃点吧")
    # if user_sex == str("女"):
    else:
        print("女士你好，你的BMI是 " + str(user_BMI) + ",体重偏胖，但是非常完美")
else:
    if user_sex == str("男"):
        print("先生你好，你的BMI是 " + str(user_BMI) + ",你是猪吧，过度肥胖")
    # if user_sex == str("女"):
    else:
        print("女士你好，你的BMI是 " + str(user_BMI) + ",你是猪吧，过度肥胖，但是非常完美")