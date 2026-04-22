# circumference of circle = 2*pi*r
import math

radius = float(input("write the radius of circle :"))
perimeter = 2 * math.pi * radius
print(f"perimeter of circle is :{round(perimeter,2)}cm")

# area of circle - πr²
area = math.pi * radius**2
print(f"area of circle is :{round(area,2)}cm²")

# hypotenus of right tringle : karn² = base²+length²
base = float(input("enter base = "))
length = float(input("enter length = "))
hypotenue = math.sqrt(pow(base, 2) + pow(length, 2))
print(f"hypotenus of right angle tringle is : {round(hypotenue,2)}")
