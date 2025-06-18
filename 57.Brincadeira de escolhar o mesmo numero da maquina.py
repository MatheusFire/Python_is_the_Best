from time import sleep
import random
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('!Regras! \nTudo é bem simples, você tem que escolher um numero de 1 a 3')
print('Se você escolher o mesmo que o computador, você sai vitorioso !')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sleep(0.5)
print('O computador esta escolhendo seu numero...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
sleep(1)
op = 'S'
tot = 0
while op == 'S':
    n = random.randint(1, 3)
    n1=int(input('Escolha seu numero!!!: '))
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    if n1 < 3:
        if n1 == n:
            tot += 1
            print('NOSSA!, você foi incrivel, nunca imaginei que você acertaria de {} tentativa! HAHAHA'.format(tot))
            print('O numero escolhido pela maquina foi {} e o seu é {}'.format(n, n1))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        elif n1 != n:
            tot += 1
            print('HAHA, você perdeu fracassado')
            ('O numero escolhido pela maquina foi {} e o seu é {}'.format(n, n1))
            print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    else:
        print('Numero invalido!')
    op = str(input('Quer tentar denovo? [S/N]? ')).upper()
    sleep(1)