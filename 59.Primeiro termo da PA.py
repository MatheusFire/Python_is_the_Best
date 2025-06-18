prim=int(input('Digite o primeiro termo da PA: '))
razão=int(input('Digite a razão de uma PA: '))
tot=prim
cont=0
while cont <= 10:
    print('{}'.format(tot),end=' ')
    tot+=razão
    cont+=1