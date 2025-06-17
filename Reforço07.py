fra=str(input('Digite um frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase'.format(fra.count('A')))
print('A primeira letra A aparece na posição {}'.format(fra.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(fra.rfind('A')+1))