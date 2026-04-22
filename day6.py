# logical operators---
# check positive even whole no.
# num = int(input("enter a value :"))
# if num >= 0 & num % 2 == 0:
#     print(f"{num} is a positive even no.")
# elif num < 0 and num % 2 == 0:
#     print(f"{num} is negative even no.")
# elif num >= 0 and num % 2 != 0:
#     print("{num} is a positive odd no.")
# else:
#     print("{num} is a negative odd no.")

# age eligibility
age = int(input("enter your age : "))
citizen = input("you are an citizen or not(y/n) :")
if age >= 18 and citizen == "y":
    print("you are eligibile for vote")
else:
    print("you are not eligibile for vote!")

# # check login system
# username = input("enter you username : ")
# password = int(input("enter your password : "))
# if username == "admin" and password == 1234:
#     print("successfully login!")
# else:
#     print("plzz check your password & username!")

# temperature check---
temperature = int(input("Enter the temperature : "))
if temperature > 30 or temperature < 10:
    print("temperature is high or low")
else:
    print("temperature is medium!")
