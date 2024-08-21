# Owner: Ryan
# Date: 21-Aug-2024

user_input = "\nFor different age we charge differently,"
user_input += "\nHow old are you: "

while True:
    age = int(input(user_input))
    if age < 3:
        print("The ticket for age under 3 is free.")
    elif age < 12:
        print("The ticket for age under 12 is $10. ")
    else:
        print("The ticket for age over 12 is $15. ")
