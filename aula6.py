nome=(input('Qual seu nome? ')).strip() or ('Sem nome informado')
idade=(input('Qual sua idade? ')) or ('Sem idade informada')
if nome or idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espaços')
    else:
        print('Seu nome não tem espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'E a ultima letra do seu nome é {nome[-1]}')
else:
    print('Digite seu nome e idade!')
                    
