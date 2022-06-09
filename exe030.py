#Digitar um número e informar se ele é impar ou par.

num = int(input('Digite um número: '))

if (num%2)==0:
    print('{} é PAR'.format(num))
else:
    print('{} é IMPAR'.format(num))
