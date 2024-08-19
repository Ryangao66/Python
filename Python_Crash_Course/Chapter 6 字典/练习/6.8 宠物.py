# Owner: Ryan
# Date: 20-Aug-2024
# 在字典中加入字典，并且用调用value中的所有内容

""" 格式
users = {
    "wamozart" :{
        "first": "wolfgang",
        "last": "mozart",
        "location": "salzburg"
    },
    "jsbach": {
        "first": "johann",
        "last": "bach",
        "location": "eisenach"
    }
}
# 用 value["first/last"] 格式来调用
"""

pets = {
    "hazel":{
        "owner": "noah",
        "breed": "labrador",
        "color": "chocolate",
        "age": 2,
    },
    "barnie": {
        "owner": "zoe",
        "breed": "french bulldog",
        "color": "milk",
        "age": 0.5
    }
}
for pet_name, pet_info in pets.items():
    print(f"你的宠物 {pet_name.title()} 在我们这里的登记的相关记录是：")
    print(f"\t主人：{pet_info["owner"].title()}")
    print(f"\t品种：{pet_info["breed"].title()}")
    print(f"\t颜色：{pet_info["color"].title()}")
    print(f"\t年龄：{pet_info["age"]}")

