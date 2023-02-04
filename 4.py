# Write a program to enter a string and a substring. You have to print the number of times that 
# the substring occurs in the given string.String traversal will take place from left to right,
# not from right to left.
#    Sample Input
#    ABCDCDC
#    CDC
#    Sample Output
#    2
a=input('Enter the word:')
b=input('Enter the word:')
n=len(a)
m=len(b)
c=0
for i in range(0, n):
    if (f'{a[i-2]}{a[i-1]}{a[i]}')==b:
        c+=1
print(c)