# Owner: Ryan
# Date: 23-Aug-2024


orders = ["veggie classic", "spinach & corn", "chicken crispy", "chicken patty", "chicken chunks"]
finished = []

while orders:
    cooking = orders.pop()
    print(f"We are cooking your {cooking.title()} sandwich.")
    finished.append(cooking)

print("\nWe have finished the following sandwiches for you: ")
for sandwich in finished:
    print(f"\t{sandwich.title()}s")