lista=[]

while True:
    print('-'*40)
    escolha_lista=str(input('   Selecione uma opção \n[I]nserir [A]pagar [L]istar \n (Aperte "N" para sair!) ')).upper().strip()
    print('-'*40)
    
    if escolha_lista.startswith('N'):
        break
    
    if escolha_lista.startswith('I'):
        escolha_continuar='S'
        while escolha_continuar.startswith('S'):
            add=input('Diga um item para ser inserido a lista: ').upper().strip()
            lista.append(add)
            print('-'*40)
            escolha_continuar=input('Quer continuar ? \n[S]im [N]ão: ').upper().strip()
            print('-'*40)
    
    if escolha_lista.startswith('A'):
        apagar=int(input('Digite o numero do indice que quer apagar: '))
        del lista[apagar]
        print(f'O indice {apagar} foi retirado da lista')
    
    if escolha_lista.startswith('L'):
        for indice, item in enumerate(lista):
            print(f'[{indice}] {item}')
    