# Owner: Ryan
# Date: 14-Aug-2024

# dict = {"aa": "bb", "cc": "dd"}
# 键值对  {"key"： "value"}

person1 = {"first_name": "CHANDLER",
           "last_name": "bing",
           "age": "35",
           "city": "NY"}
print(person1)

print(f"First name: {person1.get("first_name").title()}")
print(f"Last name: {person1.get("last_name").title()}")
print(f"Age: {person1.get("age")}")
print(f"City: {person1.get("city")}")