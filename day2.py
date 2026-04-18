import random

print("write you value :")
value = input()
print(value)
randomValue = random.randint(1, 10)
randvalue = randomValue
print(f"your random value is {randvalue}")
if int(value) == randvalue:
    print("yourvalue is equal to random value")
else:
    print("given value not match to random value")
