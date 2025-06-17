print('Regra!')
print('-'*20)
print('Você tera que escrever uma letra, pra tentar acertar a \npalavra secreta que o computador ja escolheu')
secreta='ESCOLA'
while True:
    chute=str(input('Digite uma letra: ')).upper().strip()
    if chute in secreta:
        print(f'Você acertou a palavra {chute}')
    elif chute not in secreta:
        print('....')
    else:
        print('..')