# Owner: Ryan
# Date: 15-Aug-2024

# for x, y in dict.items():
#    printf("{x}, {y}")

favorite_numbers = {"alice": "6",
                    "bruce": "3",
                    "charlie": "7",
                    "daniel": "5",
                    "ellie": "9",
                    }

for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}")


""" 字典模板
xxx = {"": "", 
       "": "", 
       "": "", 
       "": "", 
       "": "", 
       "": "", 
       }
"""