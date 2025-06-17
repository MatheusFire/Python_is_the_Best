n1= int(input('Digite um numero: '))
n2=int(input('Digite outro numero: '))
if n1 > n2:
    print('{} É maior que {}'.format(n1,n2))
elif n1 == n2:
    print('Ambos os numeros são iguais!')
elif n1 < n2:
    print('{} é menor que {}'.format(n1,n2))