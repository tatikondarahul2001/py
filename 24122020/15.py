import math

degree = float(input("Enter the value in degrees : "))
radian = degree * 0.0174533

print("sin({}) : {}".format(degree, math.sin(radian)))
print("cos({}) : {}".format(degree, math.cos(radian)))
print("tan({}) : {}".format(degree, math.tan(radian)))
