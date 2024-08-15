# Owner: Ryan
# Date: 15-Aug-2024
# 格式
# for key, value in dict.keys():
#     print(key)


# 创造一个字典
favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
friends = ["phil", "sarah"]

# 把字典中的键值对用.keys()方式打印出来 - 不理解的方式
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")
    if "erin" not in favorite_languages.keys():
        print("Erin, please take your poll")


"""
# 把字典中的键值对用用我自己理解的方式打印出来
# 可以有和书中一样的效果

friends = ["phil", "sarah"]
for name, language in favorite_languages.items():
    print(f"Hi {name.title()}")
    if name in friends:
        print(f"\t{name.title()}, I see you love {language.title()}.")

"""

"""
# 创造一个字典，把字典中的键值对打印出来

favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
for name, language in favorite_languages.items():
    print(name.upper())
    print(language.lower())

"""



