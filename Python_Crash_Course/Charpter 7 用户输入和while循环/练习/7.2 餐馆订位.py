# Owner: Ryan
# Date: 20-Aug-2024


number_of_people = int(input("请输入就餐人数： "))
if number_of_people >= 8:
    print(f"不好意思，{number_of_people}的桌子已经预定满了、下次早点来一群土鳖。")
else:
    print(f"我们正好有地方可以给你们{number_of_people}个土鳖弄一桌。")
