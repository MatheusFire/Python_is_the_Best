def par_impar():
    if num % 2 == 0:
       return print(f'O numero {num} é par !')
    elif num % 2 != 0:
       return print(f'O numero {num} é  impar !')
esc = 'S'
try:
    while esc == 'S':
        num = int(input('Digite um numero: '))
        par_impar()

        esc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if esc == 'N':
         print('Ate depois!')
         break
        elif esc != 'S':
         print('Apenas sim e não !')


except ValueError:
    print('Algo me parece errado!') 

