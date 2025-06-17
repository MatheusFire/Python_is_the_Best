n1= int(input('Qual o ano desejado? '))
if n1 % 4 == 0 and n1 % 100 != 0 or n1 % 400 == 0:
    print('{} é um ano bissexto'.format(n1))
else:
    print('{} não é um ano bissexto'.format(n1))