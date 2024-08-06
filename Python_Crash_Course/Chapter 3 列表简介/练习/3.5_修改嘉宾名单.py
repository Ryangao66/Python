# 1. 创建一个列表[],
# 2. pop出一个元素赋值为另一个变量
# 3. print的新的变量
# Owner: Ryan
# Date: 06-Aug-2024

guest_list = ["joey", "chandler", "ross"]
print(guest_list)

popped_guest = guest_list.pop(0)
unattended = popped_guest
print(popped_guest)
print(unattended)
for person in unattended:
    print(f"{unattended.title()} cannot attend tonight's dinner.")  # 为什么打印四次？

# for person in guest_list:
#     print(f"I just received a call from {person.title()}'s agent, {person.title()} cannot attend tonight's dinner.")
