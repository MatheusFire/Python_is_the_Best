import math
n=int(input('Digite um angulo: '))
print('O angulo pedido foi:{} e seu \033[31mCosseno\033[m é {:.2f}'.format(n,math.cos(math.radians(n))))
print('O angulo pedido foi:{} e seu \033[31mSeno\033[m é {:.2f}'.format(n,math.sin(math.radians(n))))
print('O angulo pedido foi:{} e sua \033[31mTangente\033[m é {:.2f}'.format(n,math.tan(math.radians(n))))