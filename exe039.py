# Ler o ano de nascimento e informar de acordo com a sua idade:
# Se ele ainda se alista ao serviço militar.
# Se é a hora de se alistar.
# Se ja passou do tempo do alistamento.
# Também precia mostrar o tempo que falta ou que passou do prazo.

from datetime import date
dat = date.today()
anohj = dat.year

ano = int(input('Digite o seu ano de nascimento: '))
idade = anohj-ano
alis = 18 - idade
anoalist = anohj + alis


print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anohj))

if anohj-ano == 18:
    print('Você esta na idade para realizar o alistamento militar')
    print('Deve se alistar \33[1;32mIMEDIATAMENTE\33[m')
elif anohj-ano < 18:
    print('Ainda faltam {:.0f} anos para seu alistamento militar.'.format(alis))
    print('Seu alistammento militar será em {}.'.format(anoalist))
else:
    print('Já passou do prazo para seu Alistamento militar.')
    print('Você deveria ter se alistado a {:.0f} anos.'.format(idade-18))
    print('Seu alistammento militar foi em {}.'.format(ano+18))







