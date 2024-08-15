# Owner: Ryan
# Date: 06-Aug-2024


for value in range(1,5):
    print(value)

# range(1,6) 实际上是1-5
for value in range(1,6):
    print(value)

# 用range()打印str
list = ["joey", "chandler", "ross",]
list.insert(0, "monica")
list.append("Phoebe")
list.append("Rachael")
for name in range(len(list)):
    print(list[name].title())

# 用while打印str
list = ["joey", "chandler", "ross",]
list.insert(0, "monica")
list.append("Phoebe")
list.append("Rachael")

name = 0
while name < len(list):
    print(list[name].upper())
    name = name + 1
