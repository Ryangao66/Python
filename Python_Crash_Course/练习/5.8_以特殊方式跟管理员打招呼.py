# Owner: Ryan
# Date: 13-Aug-2024

# Format for this practice
"""
for:
    if:
        print
    else:
        print

"""

all_account = ["admin", "root", "super", "kali", "cisco"]
admin_account = ["admin"]

for user in all_account:
    if user in admin_account:
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again")