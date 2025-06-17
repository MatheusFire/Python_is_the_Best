import math
n=float(input('Qual o comprimeito do cateto oposto: '))
n1=float(input('Qual o comprimento do cateto adjacente '))
n2 = (n ** 2 + n1 ** 2) ** (1/2)
print('A Hipotenusa vai medir {:.2f}'.format(n2))