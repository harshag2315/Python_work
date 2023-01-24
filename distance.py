#write a program to calculate the distance between two points
import math
x1=int(input('Enter the x coordinate of 1st point:'))
y1=int(input('Enter the x coordinate of 1st point:'))
x2=int(input('Enter the x coordinate of 2st point:'))
y2=int(input('Enter the x coordinate of 2st point:'))
dis=math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f'The distance between two point is {dis}')
