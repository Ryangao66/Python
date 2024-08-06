# 1. 创建一个列表[],
# 2. print(sorted(places)) # 临时按照字母排序
# 3. print(sorted(places, reverse=True)) # 临时反向排序
# 4. places.reverse() # 永远反向排序
# 5. places.sort() # 永久按照字母排序
# 6. places.sort(reverse=True) # 永久按照字母反排序
# Owner: Ryan
# Date: 06-Aug-2024


places = ["UK", "Italy", "Spain", "Poland", "Germany", "US", "Austria", "France"]
print("\nHere's the original list: ")
print(places)

# print(sorted(places)) # 临时按照字母排序
print("\nHere's the sorted list: ")
print(sorted(places))
print("\nHere's the original list: ")
print(places)

# print(sorted(places, reverse=True)) # 临时反向排序
print("\nHere's the reversed list: ")
print(sorted(places, reverse=True))
print("\nHere's the original list: ")
print(places)

# places.reverse() # 永远反向排序
places.reverse()
print("\nHere's the original list after reverse: ")
print(places)
places.reverse()
print("\nHere's the original list: ")
print(places)

# places.sort() # 永久按照字母排序
places.sort()
print("\nHere's the original list after sort: ")
print(places)

# places.sort(reverse=True) # 永久按照字母反排序
places.sort(reverse=True)
print("\nHere's the original list after reversed sort: ")
print(places)



