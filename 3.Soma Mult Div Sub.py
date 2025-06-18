n1=int(input('Um numero: '))
n2=int(input('Outro numero: '))
s1=n1+n2
s2=n1*n2
s3=n1/n2
s4=n1+n2-n2*n1/n2
print(
    'Usando {} e {} com varios tipos de contas diferentes, conseguimos\nA Soma {}' \
    '\nA Multiplicação {}' \
    '\nA Divisão {}' \
    '\nA Subtração {}'.format(n1, n2, s1, s2, s3, s4)
)