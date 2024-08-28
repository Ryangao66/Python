# Owner: Ryan
# Date: 29-Aug-2024
# 从列表中删除特定元素

orders = ["veggie classic", "pastrami", "spinach & corn", "chicken crispy","pastrami", "chicken patty", "pastrami"]
sold_out = []

print("Pastrami has been sold out.")

while 'pastrami' in orders:
    removed = orders.remove("pastrami")

print(f"\nbut we still have {orders} in stock!")





