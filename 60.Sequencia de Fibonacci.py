t1=0
t2=1
cont=3
esc=int(input('Escolha um numero! '))
print('{} {} '.format(t1,t2),end=' ')
while cont <= esc:
    t3 = t1 + t2
    cont+=1
    print('{} '.format(t3),end=' ')
    t1=t2
    t2=t3
print('FIM')