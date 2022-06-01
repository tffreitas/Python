# Digite um número e como resultado tenha o dobro, o triplo e a raiz quadrada do número digitado.

b = int(input('Digite um número: '))
print('O número digitado foi {}.\nO dobro de {} vale {}.\nO triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}. '.format(b, b, (b*2), b, (b*3), b, (b**(1/2))))



