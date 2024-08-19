# Owner: Ryan
# Date: 19-Aug-2024

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

friends = {
    "chandler": {
        "first": "chandler",
        "last": "bing",
        "age": 32
    },
    "joey": {
        "first": "joey",
        "last": "tribbiani",
        "age": 36
    },
    "ross": {
        "first": "ross",
        "last": "geller",
        "age": 37
    },
    "phoebe": {
        "first": "phoebe",
        "last": "buffay",
        "age": 27
    },
    "monica": {
        "first": "monica",
        "last": "geller",
        "age": 30
    },
    "rachael": {
        "first": "rachael",
        "last": "green",
        "age": 29
    }
}
for username, userinfo in friends.items():
    fullname = f"{userinfo["first"].title()} {userinfo["last"].title()}"
    print(f"\tFull name: {fullname}")
    print(f"\tAge: {userinfo["age"]}")
