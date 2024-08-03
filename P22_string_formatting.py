# contacts = ["隔壁老余", "隔壁老林", "隔壁老陈", "隔壁老曾", "隔壁老李", "隔壁老张", "隔壁老王"]
# for name in contacts:
#     message = name + ": 岁始之乐，点翠画柳喜开颜。\
#                       云开雾散，良辰美景共团圆。祝福" + name + \
#                       "及家人新年快乐，平安顺逐，虎年大吉"
#     send_message(name, message)
#


# contacts = ["隔壁老余", "隔壁老林", "隔壁老陈", "隔壁老曾", "隔壁老李", "隔壁老张", "隔壁老王"]
# year = "虎"
# for name in contacts:
#     message = """
#     律回春渐，新元肇启。
#     新岁甫至，福气东来。
#     金｛0｝贺岁，欢乐祥瑞。
#     金｛0｝敲门，五福临门。
#     给｛1｝及家人拜年啦！
#     新春快乐，｛0｝年大吉
#     """.format(year, name)
#
# print(message)

# contacts = ["隔壁老余", "隔壁老林", "隔壁老陈", "隔壁老曾", "隔壁老李", "隔壁老张", "隔壁老王"]
# year = "虎"
# for name in contacts:
#
#     message = """
#     律回春渐，新元肇启。
#     新岁甫至，福气东来。
#     金｛0｝贺岁，欢乐祥瑞。
#     金{0}敲门，五福临门。
#     给｛1｝及家人拜年啦！
#     新春快乐，｛0｝年大吉!
#     """.format(current_year=year, receiver_name=name)


# print(message)

gpa_dict = {"隔壁老明":3.251, "隔壁老花":3.869, "隔壁老李":3.251, "隔壁老张":3.251,}
for name in gpa_dict:
    print("{0}你好，你的当前绩点为: {1:.1f}".format(name,gpa_dict[name]))