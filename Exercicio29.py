vig=float(input('Ola, qual a distancia da sua viagem? '))
if vig >= 200:
    print('Sua viagem parece bem longa, logo te cobraremos R$0,45 por km\nlogo sua passagem vai ficar R${:.2f}'.format(vig*0.45))
else:
    print('Sua viagem não é tão longa assim! te cobraremos R$0,50 por km\nlogo sua passagem vai ficar R${:.2f}'.format(vig*0.50))