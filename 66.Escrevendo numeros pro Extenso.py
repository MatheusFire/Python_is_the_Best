numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 
'dezesete', 'dezoito', 'dezenove', 'vinte')
escolha_do_usuario = 1 

while True:
    try:    
       #Se zero for igual ou maior que escolha_do_usuario (e) for menor ou igual a 20
        escolha_do_usuario = int(input('Digite um numero de zero a vinte: '))
            
        print(
        f'Você escolheu o numero {escolha_do_usuario}\
 e seu resultado por extenso é {numeros[escolha_do_usuario]}'
)
            
        escolha_sair = input('Deseja continuar? ').strip().upper()[0]
        if escolha_sair == 'N':
            break
        elif escolha_sair != 'S':
            print('Que ?  ')
            break 
    
    except:
        print('Algo deu errado. Tente novamente !')