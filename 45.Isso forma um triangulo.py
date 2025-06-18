seg1=float(input('Digite um seguimento: '))
seg2=float(input('Digite outro seguimento: '))
seg3=float(input('Digite o ultimo seguimento: '))
if seg1 + seg2 > seg3 and seg2 + seg3 > seg1 and seg1 + seg3 > seg2:
    print('Esses seguimentos podem virar um triangulo!')

else:
    print('Isso não forma uma triangulo')