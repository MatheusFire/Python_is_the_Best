from time import sleep
print('Escolha dois valores')
print('-'*21)
num = 1
esc = 1
while esc != 5:
    num= int(input('Digite um valor: '))
    num2= int(input('Digite outro valor: '))
    print('-'*21)
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos numeros
    [5]Sair do programa''')
    print('-' * 21)
    esc= int(input('Escolha uma das opçoes: '))
    print('-' * 21)
    if esc == 1:
        print('{} + {} = {}'.format(num, num2, num+num2))
        print('-='*21)
        sleep(1)
    elif esc == 2:
        print('{} X {} = {}'.format(num,num2,num*num2))
        print('-=' * 21)
        sleep(1)
    elif esc == 3:
        if num > num2:
            print('O maior numero é {} e o menor é {}'.format(num,num2))
            print('-=' * 21)
            sleep(1)
        elif num2 > num:
            print('O Maior numero é {} e o menor é {}'.format(num2,num))
            print('-=' * 21)
            sleep(1)
    elif esc == 5:
        print('Que pena, ate depois!')
    elif esc != 1 or 2 or 3 or 4 or 5:
        print('Opção invalida!')