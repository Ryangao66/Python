# # input是用来给用户的一些提示
# input("这里是展示给用户看的内容： ")
# user_name = input("Hi, what's your name?:")
# user_age = input("Hi, " + user_name + " How old are you?: ")
# print("It's nice to meet you, " + user_name + ", you are " + user_age + " old, I'm 3 years older than you.")

# user_age = int(input("Hi, How old are you?: "))
# user_age_after_10_years = user_age + 10
# print("You will be " + str(user_age_after_10_years) + " years old in 2034")

# BMI = weight / (height **2)
# user_weight = int(input("How heavy you are in KG?: "))
# user_height = float(input("How tall you are in M?: "))
# print("Your BMI is ", int(user_weight) / int(user_height) ** 2 )

user_weight = float(input("How heavy you are in KG?: ")) # float 可以算83.5kg
user_height = float(input("How tall you are in M?: "))
user_BMI = user_weight / user_height ** 2
print("Your BMI is " + str(user_BMI))
# print("Your BMI is ", user_BMI)