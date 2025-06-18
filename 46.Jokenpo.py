#Fazer um pedra papel tesoura
import random
print('''Você vai jogar JOKENPO
[1] Pedra
[2] Papel
[3] Tesoura!''')
esc=int(input('Qual a sua escolha? '))
comp=random.randint(1,3)
if comp == esc:
    print('Empate {}'.format(comp))
elif 2==1 or 3==1 or 2==3:
    print('Você perdeu! {}'.format(comp))
else:
    print('Ganhou {}'.format(comp))
