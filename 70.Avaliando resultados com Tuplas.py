minha_tupla= ()

for c in range(4):
    numero = int(input('Digite um numero: '))
    minha_tupla+=(numero,)
print(f'Os valores digitados foram {minha_tupla}')

if 9 in minha_tupla:
    print(f'O valor 9 apareceu {minha_tupla.count(9)} vezes')
else:
    print('O valor 9 não aparece')

posicao3 = minha_tupla.index(3)
if 3 in minha_tupla:
    print(f'O valor 3 foi encontrado na posição {posicao3 + 1}')
else:
    print('O valor 3 não aparece')

for num in range(0, len(minha_tupla)):
    pares= minha_tupla[num] % 2
    if pares == 0:
        print(f'O numero {minha_tupla[num]} é par')
    