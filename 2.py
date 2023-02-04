#Count total number of vowels in a given string.
#Count total number of vowels in a given string.
a=input('Enter the Words:')
s=len(a)
b=0
for i in range(0, s):
    if a[i]=='a':
        b+=1
    elif a[i]=='e':
        b+=1
    elif a[i]=='i':
        b+=1
    elif a[i]=='o':
        b+=1
    elif a[i]=='u':
        b+=1
if b<1:
    print('No vowel is present') 
else:
    print(f'The number of vowel are {b}')  
