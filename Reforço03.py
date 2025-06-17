nome = str(input('Qual seu nome completo?: '))
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome é minúscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) -nome.count(' ')))
print('E seu primeiro nome tem {} letras'.format(nome.find(' ')))

