ano=int(input('Qual o ano que você nasceu? '))
idade=2025-ano
atraso=idade-18
if idade < 18:
    print('Você não esta apto ao serviço militar!')
elif idade == 18:
    print('Você esta apto ao serviço militar!')
elif idade > 18:
    print('Você esta atrasado {} anos!, portanto esta apto ao serviço militar!'.format(atraso))