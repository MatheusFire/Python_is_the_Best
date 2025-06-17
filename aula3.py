#print("Matheus \"Conceição\"")
while True:
    esc1=str(input('Vamos começar ?[S/N]')).upper().strip()
    if esc1 == 'S':
        nome=str(input('Qual seu nome? ')).strip()
        sobrenome=str(input('Qual seu sobrenome? ')).strip()
        idade=int(input('Qual sua idade? '))
        ano_nascimento=int(input('Qual o ano que você nasceu?'))
        print(f'Seu nome e sobrenome são: {nome} {sobrenome}')
        print(f'Sua idade é {idade}')
        print(f'E nasceu em {ano_nascimento}')
        esc2=input(str('Deseja continuar ? [S/N]')).upper().strip()
        if esc2 == 'S':
            nome=str(input('Qual seu nome? ')).strip()
            sobrenome=str(input('Qual seu sobrenome? ')).strip()
            idade=int(input('Qual sua idade? '))
            ano_nascimento=int(input('Qual o ano que você nasceu?'))
            print(f'Seu nome e sobrenome são: {nome} {sobrenome}')
            print(f'Sua idade é {idade}')
            print(f'E nasceu em {ano_nascimento}')
            esc2=input(str('Deseja continuar ? [S/N]')).upper().strip()
        else:
            break
    else:
        break

