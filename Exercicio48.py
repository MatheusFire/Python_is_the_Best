soma= 0
cont= 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A quantidade de numeros multiplos de 3 é {}, e a soma de tudo é {} '.format(cont, soma))