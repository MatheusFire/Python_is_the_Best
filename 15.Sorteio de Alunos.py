import random
n1=str(input('Nome do primeiro aluno: '))
n2=str(input('Nome do segundo aluno: '))
n3=str(input('Nome do terceiro aluno: '))
n4=str(input('Nome do quarto aluno: '))
list=[n1,n2,n3,n4]
nome=random.choice(list)
print('Esse aluno vai apagar a lousa: {}'.format(nome))