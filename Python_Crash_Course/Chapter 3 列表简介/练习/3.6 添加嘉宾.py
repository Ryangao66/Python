# 1. 创建一个列表[],
# 2. 分别在不同位子插入元素
# Owner: Ryan
# Date: 06-Aug-2024

guest_list = ["joey", "chandler", "ross"]
guest_list.insert(0, "Monica")
guest_list.insert(2, "Phoebe")
guest_list.append("Rachael")
print(guest_list)

for person in guest_list:
    print(f"I just received a call from {person.title()}'s agent, {person.title()} cannot attend tonight's dinner.")
