# Owner: Ryan
# Date: 28-Aug-2024


orders = ["veggie classic", "spinach & corn", "chicken crispy", "chicken patty", "chicken chunks"]
finished = []

while orders:
    cooking = orders.pop()
    print(f"We are cooking your {cooking.title()} sandwich. ")
    finished.append(cooking)

print(f"\nWe have done the following orders: ")
for finish in finished:
    print(f"\t{finish.title()}")
