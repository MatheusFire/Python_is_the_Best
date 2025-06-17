
cpf_atual = '562.938.502'.replace('.','').replace('-','')

cont_regressiva = 10
conta_prim_dig = cpf_atual[0:9]
mult1=0

for cpf_conta1 in conta_prim_dig:
    mult1+=int(cpf_conta1)*cont_regressiva
    cont_regressiva-=1
dig_analis1=(mult1*10)%11
dig_1 = dig_analis1 if dig_analis1 < 9 else 0

cont_regressiva2 = 11
conta_seg_dig= conta_prim_dig+str(dig_1)
mult2=0

for cpf_conta2 in conta_seg_dig:
    mult2 += int(cpf_conta2) * cont_regressiva2
    cont_regressiva2 -= 1
dig_analis2 = (mult2*10) % 11
dig_2 = dig_analis2 if dig_analis2 < 9 else 0

print(f'{conta_prim_dig}-{dig_1}{dig_2}')
