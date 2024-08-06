# 创建一个列表，给朋友打印出来问候语
# Owner: Ryan
# Date: 04-Aug-2024

name = ["Alice", "Kirsty", "Kris", "Zoe", "Jamie"]
print(f"Morning {name[0]}, how are you?")
print(f"Morning {name[-1]}, how are you?")

message = f"Morning, {name}, how are you today?"
for person in name:
    print()


for person in name:
    print(f"Hi {person}, How's your weekend?")
