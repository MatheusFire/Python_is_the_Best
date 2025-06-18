soma=cont=0
num = int(input('Digite um numero [Caso o numero seja 999 o programa ira parar]: '))
while num != 999:
    cont += 1
    soma+=num
    num = int(input('Digite um numero [Caso o numero seja 999 o programa ira parar]: '))
print(f'Você digitou {cont} numeros e a soma entre eles foi {soma}')