# area of rectangle
# area 0f rectangle = width*lenght
width = float(input("write here width:"))
length = float(input("write here length:"))
area = width * length
print(f"area of rectangle is :{area}")

# excersize 2 - Shopping cart Program
items = input("what items you want to buy?(write useing comma(,))")
listOfItems = items.split(",")
print("items are added to cart")
print(f"and your items are here: {listOfItems}")

# excersize 3- arithmetic operations, math functions
num1 = float(input("write number1: "))
num2 = float(input("write number2: "))

print(f"addition:{num1 + num2}")
print(f"subtraction:{num1-num2}")
print(f"multiplication:{num1*num2}")
print(f"division:{num1/num2}")

if int(num1 % 2 == 0):
    print(f"{num1} is a even number")
else:
    print(f"{num1} is a odd number")

# Square or cube
print(f"Square of {num1} is : {num1*num1}")
print(f"Cube  of {num1} is : {num1*num1*num1}")
print(f"Square of {num2} is : {num2*num2}")
print(f"Cube  of {num2} is : {num2*num2*num2}")

if num1 > num2:
    print(f"{num1} is the larger value")
elif num1 < num2:
    print(f"{num2} is the larger value")
else:
    print("both values are same")

num1, num2 = num2, num1

print(num1, num2)
