# Owner: Ryan
# Date: 29-Aug-2024
# 询问用户，并且把结果加入到列表中

holiday_places = []
prompt = "If you could visit one place in the world, where would you go?"
prompt += "\nEnter 'q' to quit: "

while True:
    place = input(prompt)

    if place == 'q':
        break
    holiday_places.append(place.title())

print(f"The result of the poll is:\n{holiday_places}")


"""
我的写法： 
在当需要循环提问用户的时候，需要在前面加上prompt 来使代码简洁
holiday_places = []

place = input("If you could visit one place in the world, where would you go? type 'q' to quit: ")
while True: # 否则就会有两条一样的input
    place = input("If you could visit one place in the world, where would you go? type 'q' to quit: ")

    if place == 'q':
        break
    holiday_places.append(place)

print(holiday_places)
"""




