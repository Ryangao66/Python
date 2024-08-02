house_work_count = int(input("这个月做了几次家务？： "))
red_envelope_count = int(input("这个月发了几次红包？： "))
shopping_count = int(input("这个月陪逛了几次街？： "))
has_been_angry = int(input("这个月惹生气几次？： "))

if (house_work_count > 10 and red_envelope_count > 1 and shopping_count > 4 and not has_been_angry):
    print("摩拳擦掌等待Switch")
else:
    print("让Switch随风散去...")