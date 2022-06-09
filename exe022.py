#Digitar o nome completo e como resultado mostre o nome completo com todas as letras maiusculas,
# como todas as letras minusculas  quantidade de caracteres e mostre o primeiro nome e a quantidade de letras.

nome = input('Digite seu nome Completo: ').strip()
print('Seu nome em letras maiusculas é: {}'.format(nome.upper()))
print('Seu nome em leras minusculas é: {}'.format(nome.lower()))
print('A quantidade de letras do seu nome completo é {}'.format(len(nome) - nome.count(' ')))
lst = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(lst[0], len(lst[0])))







