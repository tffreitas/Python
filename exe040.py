#Ler duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida:
# Abaixo de 5: REPROVADO!
# Entre 5 e 6.9: RECUPERAÇÃO:
# Maior ou igual a 7: APROVADO

aluno = str(input('Informe o nome do aluno: ')).capitalize()

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

print('A media do {} foi {:.1f}.'.format(aluno, media))

if media >= 7.0:
    print('{} esta \33[1;32mAPROVADO\33[m!'.format(aluno))
elif media >= 5.0 and media <= 6.9:
    print('{} esta em \33[1;33mRECUPERAÇÃO\33[m!'.format(aluno))
else:
    print('{} esta \33[1;31mREPROVADO\33[m!'.format(aluno))

