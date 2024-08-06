# 1. 创建一个列表[],
# 2. 从列表中删除元素
# Owner: Ryan
# Date: 06-Aug-2024

guest_list = ["joey", "chandler", "ross"]
guest_list.insert(0, "Monica")
guest_list.insert(2, "Phoebe")
guest_list.append("Rachael")
print(guest_list)
print("I can only have dinner with two people tonight!")
first_person = guest_list.pop()
print(f"Sorry {first_person.title()}, I can't have dinner with you tonight!")
second_person = guest_list.pop()
print(f"Sorry {second_person.title()}, I can't have dinner with you tonight!")
third_person = guest_list.pop()
print(f"Sorry {third_person.title()}, I can't have dinner with you tonight!")
fourth_person = guest_list.pop()
print(f"Sorry {fourth_person.title()}, I can't have dinner with you tonight!")
for person in guest_list:
    print(f"Good luck {person}, I'll still have dinner with you! Just don't forget to bring money to pay the bill. (:")

del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)


# for person in guest_list:
#     print(f"I just received a call from {person.title()}'s agent, {person.title()} cannot attend tonight's dinner.")
