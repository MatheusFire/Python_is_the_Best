menor = 0
maior = 0
for p in range(1,6):
    peso = float(input('Peso da {} pessoa '.format(p)))
    if p == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso    > maior:
            maior = peso
print('{} esse é o maior peso'.format(maior))
print('{} E esse o menor peso'.format(menor))