esc='S'
cont=soma=maior=menor=0
divisão=1
while esc == 'S':
    num=int(input('Escolha um numero: '))
    cont += 1
    soma += num
    divisão = soma / cont
    if cont == 1:
        menor= maior =num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    esc = str(input('Deseja continuar [S/N] ')).upper().strip()
print('Você digitou {} numeros e a media deles foi {}'.format(cont,divisão))
print('O maior valor foi {} e o menor foi {}'.format(maior,menor))