# Owner: Ryan
# Date: 22-Aug-2024


# 创建一个待验证的用户列表
unconfirmed_users = ["alice", "brian", "candace"]
# 创建一个已经验证的空列表
confirmed_users = []

# 验证每一个用户，直到没有验证的用户为止
while unconfirmed_users:
    # 把unconfirmed列表中最后一个提取出来
    current_user = unconfirmed_users.pop()
    # 将每个验证过的用户都移到已验证的列表中
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


