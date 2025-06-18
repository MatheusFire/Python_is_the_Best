Alt=float(input('Qual a altura da sua parede?: '))
Larg=float(input('Qual a largura da sua parede?: '))
print('Analisando sua parede....')
area=(Alt)*(Larg)
print('Sua parede tem {} de Altura! e {} de Largura!, então sua Area é {}'.format(Alt, Larg, area))
print('E caso queria pinta-la...')
tinta=(area)/2
print('E para pintar, você precisa de {} de tinta'.format(tinta))