# Owner: Ryan
# Date: 13-Aug-2024


current_users = ["alice", "sophie", "nicola", "zoe", "barbara"]
new_users = ["beth", "rachael", "Sophie", "sue", "Alice"]

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Username {new_user} has been taken. Please use another one.")
    else:
        print(f"{new_user} is available.")

