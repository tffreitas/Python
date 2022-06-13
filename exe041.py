#Ler o ano de nascimento de um atleta e mostrar sua categoria de acordo com a idade:
# Até 9 anos : MIRIM
# Até 14 anos : INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima : MASTER

from datetime import date
dat = date.today().year #Ano atual.

ano = int(input('Informe o ano de nascimento do Atleta: '))
idade = dat - ano

if idade <= 9:
    print('O atleta tem {} anos de idade, esta na categoria \33[1;32mMIRIM\33[m.'.format(idade))
elif idade > 9 and idade <= 14:
    print('O atleta tem {} anos de idade, esta na categoria \33[1;32mINFANTIL\33[m'.format(idade))
elif idade > 14 and idade <= 19:
    print('O atleta tem {} anos de idade, esta na categoria \33[1;32mJUNIOR\33[m'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos de idade, esta na categoria \33[1;32mSÊNIOR\33[m'.format(idade))
else:
    print('O atleta tem {} anos de idade, esta na categoria \33[1;32mMASTER\33[m'.format(idade))