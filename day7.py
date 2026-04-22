# number range check :
num = int(input("enter a number : "))
if 10 <= num <= 50:
    print("number lies between 10 to 50")
elif num < 10:
    print("value is less then 10!")
else:
    print("value is grater then 50!")

# Divisibility Check - Check if number is divisible by:3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("number is divisible by 3 and 5 both")
elif num % 3 == 0:
    print("numbe is divisible by only 3")
elif num % 5 == 0:
    print("number is divisible by only 5")
else:
    print("number is not divisible by 3 and 5 both")
