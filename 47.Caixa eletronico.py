esc1=float(input('Digite o valor do produto: '))
print('Escolha sua forma de pagamento!')
print('''[ 0 ] Dinheiro/Cheque!
[ 1 ] A vista no cartão!
[ 2 ] 2x no cartão!
[ 3 ] 3x ou mais no cartão!''')
esc=int(input(' '))
A = esc1 - ( esc1 * 10 / 100 )
B = esc1 - ( esc1 * 5 / 100 )
C = esc1

if esc == 0:  
    print('O preço vai ficar {:.2f}'.format(A))
elif esc == 1:
    print('O preço vai ficar {:.2f}'.format(B))
elif esc == 2:
    M = esc1/2
    print('O preço vai ficar {}, e sendo um total de {}'.format(M,C))
elif esc == 3:
    D = esc1 + (esc1 * 20 / 100)
    parcela=int(input('Qual vai ser a parcela? '))
    L = esc1 / parcela
    print('O valor total do produto é de {:.2f}, sofrendo um juros de 20%, ficando com {:.2f}'.format(esc1,D))
    print('E o valor de seus parcelas serão de {:.2f} correspondentes a {:.2f} parcelas'.format(L,parcela))
else:
    print('Opção invalida !')