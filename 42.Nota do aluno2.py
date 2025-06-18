nota1=float(input('Qual a primeira nota do aluno? '))
nota2=float(input('Qual a segunda nota do aluno? '))
nota3=float(input('Qual a terceira nota do aluno? '))
nota4=float(input('Qual a quarta nota do aluno? '))
soma = nota1+nota2+nota3+nota4
resul = soma / 4
if resul < 5.0:
    print('Sua nota foi {:.1f}, e infelizmente ela é muito baixa pra te passar de ano'.format(resul))
elif resul >= 7.0:
    print('Que nota incrivel! {:.1f} isso faz você passar de ano com louvor!'.format(resul))
elif resul >= 5.0 :
    print('Sua nota foi {:.1f}, rasuavel pra você poder passar de ano!, parabens'.format(resul))
