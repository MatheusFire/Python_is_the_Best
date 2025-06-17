from random import randint
from time import sleep
print('-='*11)
print('Vamos jogar impar ou par')
print('-='*11)
v=0
while True:
    jog=int(input('Escolha um numero de 0 a 10: '))
    comp=randint(0,10)
    tot=jog+comp
    tipo=' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]:  ')).strip().upper()[0]
    print(f'Você escolheu {jog} e o Computador escolheu {comp} e o Total é {tot}')
    if tipo == 'I':
        if tot % 2 == 0:
            print('O Jogador perdeu!')
            break
        elif tot % 2 != 0:
            print('O Jogador ganhou!')
            v += 1
    elif tipo == 'P':
        if tot % 2 == 0:
            print('O Jogador ganhou!')
            v += 1
        elif tot % 2 != 0:
            print('O jogador perdeu!')
            break
print(f'Você venceu {v} vezes!')



