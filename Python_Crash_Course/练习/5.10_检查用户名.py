# Owner: Ryan
# Date: 13-Aug-2024

# Format for this practice
"""
if:
    for:
        if:
            print
        else:
            print
else:
    print
"""

current_users = ["alice", "sophie", "nicola", "zoe", "barbara"]
new_users = ["beth", "rachael", "sophie", "sue", "alice"]

for new_user in new_users:
    if new_user in current_users:
        print(f"Username {new_user} has been taken. Please use another one.")
    else:
        print(f"{new_user} is available.")

