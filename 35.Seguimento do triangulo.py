print('Formando o seguimento de um Triangulo!')
a=float(input('Digite um numero: '))
b=float(input('Digite outro numero: '))
c=float(input('Digite mais um numero: '))
if a+b > c and b+c > a and a+c > b:
    print('Esse seguimento a cima PODE ser um triangulo!')
else:
    print('Esse seguimento acima NÃO vai ser um triangulo')