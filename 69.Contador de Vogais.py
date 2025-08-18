contador = 0
while True:
    palavra = input('Digite uma palavra: ').upper()
    
    esc = str(input('Quer substituir a palavra anterior? [S/N] ')).strip().upper()
    if esc == 'S' :   
        print('OK')
    
    elif esc == 'N': 
        print('Manteremos a palavra anterior')
        for p in palavra:
            if p in 'AEIOU':
                contador+=1
               
        print(f'\nAs vogais na palavra {palavra} são',end=' ')
        print(f'\n{contador}',end=' ')
        break
            
    
    else:
        print("Não peguei a ideia, apenas 'S' ou 'N' ")
        break
#ainda a corrigir !