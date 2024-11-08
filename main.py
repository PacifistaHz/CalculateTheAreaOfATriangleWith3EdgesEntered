a=input("Enter a A edge: ")
b=input("Enter a B edge: ")
c=input("Enter a C edge: ")
a=float(a)
b=float(b)
c=float(c)

u=(a+b+c)/2
import math
area=math.sqrt(u*(u-a)*(u-b)*(u-c))

print("Area of triangle is: {0}".format(area))