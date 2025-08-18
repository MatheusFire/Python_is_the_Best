print('Soma!')
def soma(n1, n2):
            print(f'Somando o numero {n1}, e o numero {n2}, o resultado é {n1+n2}')           
while True:
    try:
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite outro numero: '))

        soma(n1, n2)
        
        escolha = input('[S/N] Quer continuar a somar? ').strip().upper()[0]
        if escolha == 'N':
            break
        elif escolha != 'S':
            print('Não consegui entender...')
            break
    
    except ValueError:
        print('Algo esta fora do conforme, tente denovo')
        
            