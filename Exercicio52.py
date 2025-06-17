from datetime import date
atual = date.today().year
maiores = 0
menores = 0
for c in range(1,8):
    ano=int(input('Qual ano nasceu a {} pessoa'.format(c)))
    idade= atual - ano
    if idade > 18:
        maiores += 1
    else:
        menores += 1
print('{} São maiores de 18'.format(maiores))
print('{} São menores de 18'.format(menores))