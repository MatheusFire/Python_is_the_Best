# def multiplicador(x):
#     def primeiro_vezes_2 (y):
#         return x*y
#     return primeiro_vezes_2

# vezes2 = multiplicador(2)
# print(f'Eu estou duplicando {vezes2(5)}')

# def triplicador(o):
#     def primeiro_vezes_3 (y):
#         return o*y  
#     return primeiro_vezes_3

# vezes3 = triplicador(3)
# print(f'Eu estou triplicando {vezes3(5)}')

# def quadruplicaodr(p):
#     def primeiro_vezes_4 (y):
#         return p*y
#     return primeiro_vezes_4

# vezes4 = quadruplicaodr(4)
# print(f'Eu estou quadruplicando {vezes4(5)}')

# for c in range(2,101):
#     def multiplicador(x):
#         def primeiro_multiplo():
#             return x*c
#         return primeiro_multiplo
#     vezes = multiplicador(5)
#     print(f'{vezes()}')
#É legal brincar com def, sei que o multiplicador ate o quadriplicador eu poderia ter feito de forma mais efetiva como
def multiplicar(multiplicador):
    def numero_multiplicado(numero):
        return multiplicador * numero
    return numero_multiplicado

vezes_2 = multiplicar(2)
vezes_3 = multiplicar(3)
vezes_4 = multiplicar(4)

print(vezes_2(5))
print(vezes_3(5))
print(vezes_4(5))
#Mas tudo em ordem de aprender !!!