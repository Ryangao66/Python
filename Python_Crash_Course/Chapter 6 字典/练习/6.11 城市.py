# Owner: Ryan
# Date: 20-Aug-2024
# 在字典中加入列表，并且用for loop打印出所有列表内容

cities = {
    "vienna": {
        "country": "austria",
        "population": "1.8 million",
        "fact": "is the capital city of "
    },
    "athens": {
        "country": "greece",
        "population": "600,000",
        "fact": "is one of the world's oldest cities"
    },
    "rome": {
        "country": "italy",
        "population": "2.8 million",
        "fact": "is a must visit city"
    }
}

# 用for loop 把所有的key全打印出来
print("今天我们将要讲诉三个城市，分别是：")
for city_names, city_infos in cities.items():
     print(f"\t{city_names.title()}")

# 把key值定义为一个变量，然后打印出里面的内容
print("\n首先来介绍第一个城市Vienna: ")
vienna = cities["vienna"]
print(f"Vienna {vienna["fact"]}{vienna["country"].title()}, with a population of {vienna["population"]}. ")

# 把key值定义为一个变量，然后打印出里面的内容
print("\n接下来来介绍第二个城市Athens: ")
athens = cities["athens"]
print(f"Athens {athens["fact"]} in {athens["country"].title()}, with a population of {athens["population"]}. ")

# 把key值定义为一个变量，然后打印出里面的内容
print("\n最后来介绍第三个城市Rome: ")
rome = cities["rome"]
print(f"Roma {rome["fact"]} in {rome["country"].title()}, with a population of {rome["population"]}. ")


