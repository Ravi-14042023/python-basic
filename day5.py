# calculator ----
value1 = float(input("enter value1 : "))
sign = input("enter an sign(+,-,*,/,%) : ")
value2 = float(input("enter value2 : "))

if sign == "*":
    print(value1 * value2)
elif sign == "+":
    print(value1 + value2)
elif sign == "-":
    print(value1 - value2)
elif sign == "/":
    print(round(value1 / value2, 2))
elif sign == "%":
    print(value1 % value2)
else:
    print("plzz enter a valid operator(sign)!")

# convert temperature - celcius to fahrenheit , fahrenheit to celcius!
# celcius to fahrenheit formula = (°C × 9/5) + 32 = °F
# fahrenheit to celcius formula = (°F − 32) × 5/9 = °C


temperature = float(input("what is the temperature : "))
unit = input("unit of temperature(C/F) : ")
if unit == "C":
    cnvrtinfaranhite = (temperature * (9 / 5)) + 32
    print(f"temperature in faranhite is : {round(cnvrtinfaranhite,2)}°F")
elif unit == "F":
    cnvrtincelcius = (temperature - 32) * 5 / 9
    print(f"temperature in celcius is : {round(cnvrtincelcius,2)}°C")
else:
    print("pzz enter valid unit of temperature(in capital(C/F))!")
