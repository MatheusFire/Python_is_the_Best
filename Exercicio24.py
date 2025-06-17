dia=float(input('Quantos dias você ficou com o veiculo: '))
km=float(input('E quantos km percorreu com o mesmo: '))
dias=dia*60
kms=km*0.15
resul=dias+kms
print('Você ficou {} dias com o veiculo e percorreu {}km \nLogo você deve {}R$ pelos dias e {}R$ pelos km rodados'.format(dia, km, dias, kms))
print('Então o preço total a pagar é {}R$'.format(resul))