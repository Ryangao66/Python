# Owner: Ryan
# Date: 15-Aug-2024
# 格式
# for key in sorted(dict.keys():
#     print(key)


# 创造一个字典
favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
friends = ["phil", "sarah"]
# 按照 A-Z 的方式打印
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# 按照 A-Z 的方式打印 value
for name in sorted(favorite_languages.values()):
    print(f"{name.title()}, thank you for taking the poll.")