# Owner: Ryan
# Date: 20-Aug-2024
# 在字典中加入列表，并且用for loop打印出所有列表内容

favorite_numbers = {
    "alice": [6, 3, 5],
    "bruce": [9, 2, 1],
    "charlie": [7, 5, 2],
    "daniel": [7, 0, 5],
    "ellie": [3, 2, 8],
}
for names, numbers in favorite_numbers.items():
    print(f"{names.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f"\t{number}")
