from datetime import date
atual = date.today().year
ano=int(input('Qual ano que você nasceu? '))
idade= atual - ano
if idade <= 9:
    print('Você tem {} \nVocê é um atleta mirim!'.format(idade))
elif idade <= 14:
    print('Você tem {} \nVocê é um atleta juvenil!'.format(idade))
elif idade <=19:
    print('Você tem {} \nVocê é um atleta junior!'.format(idade))
elif idade == 20:
    print('Você tem {} \nVocê é um atleta sênior!'.format(idade))
elif idade <= 110:
    print('Você tem {} \nParabens!, você é um atleta MASTER'.format(idade))
elif idade >= 111 :
    print('Você tem {} \nE tu ta vivo?!'.format(idade))