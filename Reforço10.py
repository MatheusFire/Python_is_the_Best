print('Divisores de um Numero!')
num=int(input('Digite um numero que sera dividido: '))
num2=int(input('Digite um numero que sera o total da divisão: '))
tot=0
for c in range(1,num2+1):
    if num % c == 0:
        tot+=0
        print('\033[36m',end=' ')
        print('{}'.format(c), end=' ')