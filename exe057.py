#Programa para registrar o Sexo, M ou F, só vai parar de perguntar o sexo quando o usuario digitar o valor M ou F.


sexo = str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo [M/F]: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso!'.format(sexo))
