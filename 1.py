#Write a program to count and display the number of capital letters in a given string.
a=input('Enter the sentence:')
s=len(a)
c=0
for i in range(0, s):
    if a[i].isupper()==True:
        print(a[i], end='\t')
        c+=1
print(f'\nThe number of character in upper case is {c}')