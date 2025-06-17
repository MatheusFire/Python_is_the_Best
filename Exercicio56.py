import math
esc=int(input('Escolha um numero: '))
c=esc
x=1
print('{}'.format(esc), end='')
while c > 1:
    print(' X {}'.format(c,),end='')
    x*= c
    c -= 1
print('= {}'.format(x))
