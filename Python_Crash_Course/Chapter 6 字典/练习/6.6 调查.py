# Owner: Ryan
# Date: 15-Aug-2024
# 格式
# for key, value in dict.items():
#     print(key)
#     print(value)


favorite_languages = {"jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    "alice": "c#",
    "zoe": "java",
    "ben": "php"
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n")
coders = ["ryan", "kris", "alice", "Nick", "Jamie", "phil"]
for coder in coders:
    if coder in favorite_languages.keys():
        print(f"Thank you for taking the survey, {coder.title()}")
    else:
        print(f"{coder.title()}, what's your favorite language?: ")
