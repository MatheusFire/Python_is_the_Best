peso=float(input('Qual seu peso? '))
altura=float(input('Qual sua altura? '))
imc = peso/ (altura * altura)
if imc < 18.5:
    print('Seu imc é {:.1f}, então esta abaixo do seu peso!'.format(imc))
elif imc < 25:
    print('Seu imc é {:.1f}, então esta no peso ideal ! Parabens!'.format(imc))
elif imc < 30:
    print('Seu imc é {:.1f}, então esta acima do peso! Cuidado!'.format(imc))
elif imc < 40:
    print('Seu imc é {:.1f}, VOCÊ ESTA OBESO! TOME CUIDADO!'.format(imc))
elif imc > 40:
    print('Seu imc é {:.1f}, AQUI A DIETA DEIXOU DE SER OPÇÃO E VIROU NESCESSIDADE!'.format(imc))