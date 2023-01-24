#calculate the area of triangle using heron's formula
import math
a=float(input('Enter the first side of triangle:'))
b=float(input('Enter the second side of triangle:'))
c=float(input('Enter the third side of triangle:'))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'The area of traingle using a heron\'s formula is {area}')