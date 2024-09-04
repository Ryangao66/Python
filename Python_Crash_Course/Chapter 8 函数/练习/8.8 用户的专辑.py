# Owner: Ryan
# Date: 05-Sep-2024
# 定义函数，然后用while循环
# 然后把用户输入的信息储存在字典中

favorite_alums = {}

def make_album(singer, album):
    album = {"singer": singer, "album": album}
    return album


while True:
    print("\nWho's your favorite singer and which album you like the most: ")
    print("Enter 'q' to quit.")
    singer = input("Singer: ")
    if singer == 'q':
        break

    album = input("Album: ")
    if album == 'q':
        break
    favorite_alums[singer.title()] = album.title()

print(favorite_alums)