# Owner: Ryan
# Date: 07-Aug-2024

players = ['totti', 'de rossi', 'florenzi', 'mancini', 'perrotta', 'taddei', 'juan']
for name in players:
    print(name.title())

# 打印前三个
print("The first three players are:")
print(players[:3])

# 打印中间三个
print(len(players))
print("\nThree players from the middle of the list are:")
print(players[2:5])

# 打印最后三个
print("\nThe last three players in the list are:")
print(players[4:])

