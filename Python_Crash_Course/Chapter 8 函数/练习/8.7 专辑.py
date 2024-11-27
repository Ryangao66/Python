# Owner: Ryan
# Date: 05-Sep-2024
# 定义函数，然后返回字典

def make_album(singer, album):
    album = {"singer": singer.title(), "album": album.title()}
    return album


album_01 = make_album("Leslie cheung", "monica")
album_02 = make_album("Jacky cheung", "amour")
album_03 = make_album("Eason Chan", "U87")
print(album_01, album_02, album_03)
print(f"{album_01}, \n{album_02}, \n{album_03}")