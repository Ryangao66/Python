# Owner: Ryan
# Date: 20-Aug-2024
# 在字典中加入列表，并且用for loop打印出所有列表内容

favorite_places = {
    "ryan": ["roma", "vienna", "salzburg", "athens"],
    "alice": ["london", "paris", "madrid", "venice"],
    "brad": ["miami", "munich", "milan", "los angeles"]
}
for names, places in favorite_places.items():
    print(f"{names.title()}'s favorites are: ")
    for place in places:
        print(f"\t{place.title()}")


