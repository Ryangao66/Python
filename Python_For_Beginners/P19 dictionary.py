# contacts = {("Rachael", "Prophecy"): "0278801111",
#             "Nigel": "0228802222",
#             ("Rachael", "MrApple"): "2008803333",  # 元组example_tuple = ("姓名" , "部门")
#             ("Aaron", "IT"): "0218804444",
#             "Kris": "0278805555",
#             ("Aaron", "Security"): "02878806666"}
# del contacts["Nigel"]
# len(contacts)
#
# print("Kris" in contacts)
# print("Chris" in contacts)

# 结合input、字典、if判断，做一个查询流星雨含义的电子词典程序
slang_dict = {"显眼包": "显眼包，来自地方方言，也可以写成“现眼包”，东北方言有，丢人现眼，一词.",
              "哈基米": "哈基米原意是日语中的“蜂蜜”，但因为被用来给拍摄的可爱动物视频做配乐而爆火，用来形容可爱的生物，如猫咪和小狗等。例如，看到一只特别可爱的猫咪视频，你可以评论说“这只猫咪太哈基米了！”",
              "美拉德穿搭": "指以棕色、褐色为主的穿搭风格，成为一种网络流行的穿衣风格。",
              "特种兵式旅游": "这是一种压缩旅游时间，但不压缩行程的旅游方式。主打的是行程紧、强度高、任务重、口袋穷。",
              "电子榨菜": "电子零食。它将短视频、表情包和社交媒体帖子等轻松内容比作下饭零食，而非主餐。",
              "内卷": "原指一类文化模式达到了某种最终的形态以后，而只能不断地在内部变得更加复杂的现象。现指同行间竞相付出更多努力以争夺有限资源，从而导致个体“收益努力比”下降的现象。",
              }

slang_dict["尊嘟假嘟"] = "出自博主@伯恩山bot，模仿小猫小狗的说话方式，谐音\"真的假的\"。 这是尊嘟O.O，这是假嘟o.o，所以尊嘟假嘟是O.o"
slang_dict["芭比Q"] = "谐音barbecue，原意为烧烤，在网络用语中“芭比q了”意为“完蛋了”。"
slang_dict["泰裤辣"] = "源自于某艺人在音乐节中一段激情但比较词穷的演讲，他本意是激励别人做自己想做的事，话到了嘴边又停顿很多遍，最后高喊了一句“泰酷辣（太酷啦）”作为结束。 由于比较洗脑又可以运用到各种场景",
slang_dict["鸡哔你"] = "来自博主@阿基米德，谐音“击毙你”。因为这位博主很爱在视频中说“击毙你“三个字，由于他独特的发音，听上去是“鸡哔~你”而成为网络热梗。",
slang_dict["city walk"] = "这个词汇指的是在城市里漫步的活动，是一种通过步行的方式探索城市大街小巷的生活休闲方式。它强调了对城市环境的探索和发现，是一种健康而有趣的生活方式",

query = input("请输入你想要查询的流行语: ")
if query in slang_dict:
    print("您查询的" + query + "含义如下")
    print(slang_dict[query])
else:
    print("您查询的流行语暂未收录。")
    print("当前本词典收入的词条数为： " + str(len(slang_dict)) + "条。")


# 创造一个字典，把字典中的键值对打印出来

favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
for name, language in favorite_languages.items():
    print(name.upper())
    print(language.lower())


# 创建一个字典
favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
print(favorite_languages)
# 在字典中取特定值
print(f"Sarah favorite language is {favorite_languages["sarah"].title()}.")
