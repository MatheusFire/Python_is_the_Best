vcasa= float(input('Qual o valor da casa? '))
salario= float(input('Qual o seu salario? '))
anos= float(input('Quantos anos você quer pagar a casa? '))
prestação = vcasa / (anos * 12)
limite = salario * 30 / 100
if prestação <= limite:
    print('Ok')
else:
    print('nop')