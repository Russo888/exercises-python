import random
MAIUSCOLE= ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
MINUSCOLE=('abcdefghijklmnopqrstuvwxyz')
NUMERICHE= ('0123456789')

password=['','','','','','','','','','']

MaiuMinu=MAIUSCOLE+MINUSCOLE
tutto=MAIUSCOLE+MINUSCOLE+NUMERICHE
password[0]=random.choice(MaiuMinu)

for i in range (9):
    password[i+1]=random.choice(tutto)

print ("Password non censurata: ")
print (password)

for i in range (4):
    password[i]='*'

passwordStr=''.join(password)
print ("Password censurata: ")
print (passwordStr)
