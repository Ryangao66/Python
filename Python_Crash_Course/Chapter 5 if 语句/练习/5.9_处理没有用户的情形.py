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

all_account = []

if all_account:
    for user in all_account:
        if user in all_account:
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again")
else:
    print(f"We need to find some users!")