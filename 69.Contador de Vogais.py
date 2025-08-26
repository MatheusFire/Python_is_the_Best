contador = 0
vogais = ('A','E','I','O','U')
nova_vogal = []
while True:
    palavra = input('Digite uma palavra: ').upper()
    
    esc = str(input('Quer substituir a palavra anterior? [S/N] ')).strip().upper()
    if esc == 'S' :   
        print('OK')
    
    elif esc == 'N': 
        print('Manteremos a palavra anterior')
        for p in palavra:
            if p in vogais:
                nova_vogal.append(p)
        print(f'As vogais na palavra {palavra} são {', '.join(map(str, nova_vogal))}')
        break
            
    else:
        print("Não peguei a ideia, apenas 'S' ou 'N' ")
        break
