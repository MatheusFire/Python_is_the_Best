mul=int(input('Qual a velocidade do veiculo? '))
resul= mul - 80
mi= resul * 7
if mul>= 80:
    print('Seu veiculo esta muito rapido! \nEm retalhação a isso você recebera uma multa de {}R$!'.format(mi))
else:
    print('Ok')