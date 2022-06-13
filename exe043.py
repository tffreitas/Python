# Ler o peso e altura de uma pessoal e calcule seu IMC e mostre o STATUS conforme tabela abaixo:
#Abaixo de 18.5 : Abaixo do Peso
#Entre 18.5 e 25: peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida.

ps = float(input('Informe o peso (kg): '))
alt = float(input('Informe a altura (m): '))

imc = ps/alt**2

if imc < 18.5:
    print('O IMC é {:.1f}, Você esta na faixa de peso \33[1;31mABAIXO DO PESO\33[m.'.format(imc))
elif 18.5 <= imc < 25:
    print('O IMC é {:.1f}, Você esta na faixa de peso \33[1;32mIDEAL\33[m.'.format(imc))
elif 25 <= imc < 30:
    print('O IMC é {:.1f}, Você esta na faixa de peso \33[1;33mSOBREPESO\33[m.'.format(imc))
elif 30 <= imc < 40:
    print('O IMC é {:.1f}, Você esta na faixa de peso \33[1;31mOBESIDADE\33[m.'.format(imc))
else:
    print('O IMC é {:.1f}, Você esta na faixa de peso \33[1;31;107mOBESIDADE MÓRBIDA\33[m.'.format(imc))

