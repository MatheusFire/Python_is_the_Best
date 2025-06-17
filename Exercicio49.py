soma = 0
amos = 0
for c in range(0,6):
    intei=int(input('Digite um numero! '))
    if intei % 2 == 0:
        soma += intei
    else:
        amos += intei
print('A soma de todos os numero pares são {} e dos numero impares são {}'.format(soma, amos))
