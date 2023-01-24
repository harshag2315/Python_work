import math
print('Enter the coefficient of a quadratic equation with signs:')
a=int(input('Enter the coefficient of x^2='))
b=int(input('Enter the coefficient of x='))
c=int(input('Enter the coefficient of numeric part='))
r1=4*a*c
div=2*a
if a<0 and c<0: 
    root1= ((-1)*(b*b)-math.sqrt(r1))/div
    root2= ((-1)*(b*b)+math.sqrt(r1))/div
    print('The Quadratic equation has real roots:')
    print('Root1=',root1,'\nRoot2=' , root2)
elif a<0 or c<0:
    print('The  quadratic equation has imaginary roots:')
    root3=((-1)*(b*b))
    print('Root1=(', root3,'+',(-1)*r1,'i)/',div)
    print('Root2=(', root3,'-',(-1)*r1,'i)/',div)
else:
    root1= ((-1)*(b*b)-math.sqrt(r1))/div
    root2= ((-1)*(b*b)+math.sqrt(r1))/div
    print('The Quadratic equation has real roots:')
    print('Root1=',root1,'\nRoot2=' , root2)