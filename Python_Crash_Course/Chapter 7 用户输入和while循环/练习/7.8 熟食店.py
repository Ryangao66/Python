# Owner: Ryan
# Date: 23-Aug-2024
# 1. 创建一个order list
# 2. 把order里面的元素单独提取出来，放入到一个新的finished list里面，然后打印出来告诉客户正在准备他们的披萨
# 3. 用for循环把所有在finished list里面的元素打印出来，告诉客户所有完成了的订单

orders = ["veggie classic", "spinach & corn", "chicken crispy", "chicken patty", "chicken chunks"]
finished = []

while orders:
    # pop出来的元素设置为新的变量
    cooking = orders.pop()
    print(f"We are cooking your {cooking.title()} sandwich.")
    # pop 出来的元素加入到新的list
    finished.append(cooking)

print("\nWe have finished the following sandwiches for you: ")
for sandwich in finished:
    print(f"\t{sandwich.title()}s")