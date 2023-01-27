#Write a code to determine the character entered by the user
char=input('Press an key:')
if(char.isalpha()):
    print('The user has entered a chacter')
if(char.isdigit()):
    print('The user has entered a digit')
if(char.isspace()):
    print('The user has entered space')
else:
    print('The user has entered symbol')