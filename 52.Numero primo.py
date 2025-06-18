intei = int(input('Digite um numero! '))
tot = 0
for c in range(1,intei+1,1):
    if intei % c == 0:
        tot += 1
        print('\033[36m',end=' ')
        print('{}'.format(c), end=' ')
    else:
        print('\033[31m', end=' ')
        print('{}'.format(c), end=' ')
if tot == 2:
    print('\n\033[m{} é um numero primo!'.format(intei))
else:
    print('\n\033[m{} não é um numero primo!'.format(intei))