#DIgitar nome completo e após isso ter como Resposta somente Primeiro e Ultimo nome

nome = str(input('Digite seu nome completo: ')).strip().upper()
lst = nome.split()
print('Seu primeiro nome é: {}'.format(lst[0]))
print('Seu ultimo nome é: {}'.format(lst[len(lst)-1]))


