# Owner: Ryan
# Date: 15-Aug-2024
# 格式
# for value in sorted(dict.values():
#     print(value)
# 删除重复格式
# for key in set(dict.keys():
#     print(key)



# 创造一个字典
favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }

# 打印出字典中所有的values
print("The following languages have been mentioned:")
for languages in favorite_languages.values():
    print(languages.title())

# 用set()删除重复项
print("\nThe following languages have been mentioned:")
for languages in set(favorite_languages.values()):
    print(languages.title())