# Escrever um programa que leia a velocidade de um carro. Se ultrapassar 80Km/h, mostra uma
# msg informando que ele foi multado. A multa custa R$ 7 a cada Km/h que passar do limite.

vlc = float(input('Informe a velocidade que esta o carro: '))
if vlc>80:
    print('MULTADO! você esta acima do limite de velocidade. O limite é 80Km/h')
    print('A multa que deverá pagar é de R$ {:.2f}'.format((vlc-80)*7))
else:
    print('Tenha um bom dia, diriga com segurança!')



