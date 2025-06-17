import random
print('Regras!'.upper())
print('As contas serão feitas invertidas e mostrara o resultado maior e menor'.capitalize())
print('+'*20)
a=int(input('Digite um numero '))
b=int(input('Digite outro numero '))
c=int(input('Digite mais um numero '))
d=a+c
e=b+b
f=c+a
menor = d
if e<d and e<f:
    menor = e
if f<d and f<e:
    menor= f
print('{} É o menor numero!'.format(menor))
maior = d
if e>d and e>f:
    maior = e
if f>d and f>d:
    maior = f
print('{} É o maior numero!'.format(maior))