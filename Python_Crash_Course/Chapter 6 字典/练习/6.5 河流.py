# Owner: Ryan
# Date: 15-Aug-2024

# dict = {"aa": "bb", "cc": "dd"}
# 键值对  {"key"： "value"}

rivers = {"nile": "egypt",
       "amazon": "brazil",
       "thames": "london",
       "waikato": "hamilton",
       "danube": "vienna",
       }
for name, city in rivers.items():
    print(f"{name.title()} runs through {city.title()}")

# 只打印key值
print("\n# 只打印key值")
for name in rivers.keys():
    print(f"\t{name.title()}")

# 只打印value值
print("\n# 只打印value值")
for city in rivers.values():
    print(city.title())