# Gerar valor para o aluguel de um carro passando a KM rodada e os dias alugados.
# Diaria do carro R$ 60
# KM rodado R$ 0,15

diaria = int(input('Digite quantas diarias foram utilizadas: '))
km = float(input('Digite quantos quilômetros foram rodados com o veículo: '))
print('Foram utilizados {:.0f} diarias do veículo e rodados {:.2f} quilometros. O valor a pagar é R$ {:.2f}'.format(diaria, km, ((diaria*60)+(km*0.15))))
