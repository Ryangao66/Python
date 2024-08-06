# 1. 创建一个列表[],
# 2.
# 3.
# Owner: Ryan
# Date: 06-Aug-2024

guest_list = ["joey", "chandler", "ross"]
guest_list.insert(0, "rachael")
guest_list.append("phoebe")
guest_list.insert(2, "monica")
print("Here's the guest list of tonight's dinner!")
for name in guest_list:
    print(name.title())

num = len(guest_list)
print(f"There wil be {num} person come here to have dinner with you!")


# for person in guest_list:
#     print(f"I just received a call from {person.title()}'s agent, {person.title()} cannot attend tonight's dinner.")
