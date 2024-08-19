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
for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    full_name = (f"{user_info["first"]} {user_info["last"]}")
    location = user_info = user_info["location"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

""" 我自己的写法
    print(f"Username: {username.title()}")
    print(f"\tFull name: {user_info["first"].title()} {user_info["last"].title()}")
    print(f"\tLocation: {user_info["location"].title()}")
"""