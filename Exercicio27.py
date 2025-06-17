import random
n=random.randint(0,5)
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('!Regras! \n|Tudo é bem simples, você tem que escolher um numero de 0 a 5')
print('Se você escolher o mesmo que o computador, você sai vitorioso !')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('O computador esta escolhendo seu numero...')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
n1=int(input('Escolha seu numero!!!: '))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
if n1 == n:
    print('NOSSA!, você foi incrivel, nunca imaginei que você acertaria')
else:
    print('HAHA, você perdeu fracassado')
print('O numero escolhido pela maquina foi {} e o seu é {}'.format(n,n1))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
if n == n1:
    print('Foi um otimo jogo campeão')
else:
    print('Tente denovo se tiver coragem')
