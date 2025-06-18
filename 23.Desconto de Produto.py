pre=float(input('Digite o preço do produto: '))
des=float(input('Digite o desconto do produto: '))
resul= pre - (pre * des / 100)
print('O preço do produto é {} e seu descontp é {} logo, seu produto fica {}'.format(pre,des,resul))