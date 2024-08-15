# Owner: Ryan
# Date: 06-Aug-2024

# 1. 创建一个列表并且用for loop打印出来
magicians = ["alice", "david", "carolina"]
for person in magicians:
    # 2. 用f可以在字符串中加入var
    print(f"{person.title()}, that was a great trick!")
    # 3. 在最后加入\n来空一行
    print(f"I can't wait to see your next trick,{person.title()}.\n")

print("Thank you, everyone. That was a great magic show!")
