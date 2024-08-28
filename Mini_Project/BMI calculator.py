# Owner: Ryan
# Date: 24-Aug-2024
# 第一个按照自己需求的作出的代码


weight = float(input("What's your weight(in KG)? "))
height = float(input("What's your height(in M)? "))


def calculate_bmi(
        weight, height):
    bmi = weight / height ** 2
    if bmi <= 18.5:
        category = "underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    print(f"Your BMI is {category}")
    return bmi


result = calculate_bmi(weight, height)
print(f"Your BMI index is {result}")

ideal_bmi = float(input("\nWhat's your ideal BMI? "))
ideal_weight = ideal_bmi * height ** 2
print("Your need to lose " + str(int(weight) - int(ideal_weight)) + "kg")
