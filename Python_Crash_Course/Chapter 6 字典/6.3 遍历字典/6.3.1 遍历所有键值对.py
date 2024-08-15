# Owner: Ryan
# Date: 15-Aug-2024
# 格式
# for key, value in dict.items():
#     print(key)
#     print(value)


user_0 ={"username": "efermi",
         "first": "enrico",
         "last": "fermi"}
# key, value 可以为任意值
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# 创造一个字典，然后把字典用的key, value带入到print中打印出来
favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python"
    }
for name, language in favorite_languages.items():
    print(f"{name.title()},s favorite's language is {language.title()}.")

