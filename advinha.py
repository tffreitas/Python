print("*"*32)
print("Bem vindo ao jogo da Advinhação!")
print("*"*32)

numero_secreto = 28
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    numero = int(input("Digite o numero entre 1 e 100: "))
    correto = numero == numero_secreto
    maior   = numero > numero_secreto
    menor   = numero < numero_secreto

    if (numero < 1 or numero > 100):
        print("Você deve digitar um número entre 1 e 100")
        rodada += 1
        continue

    if(correto):
        print("Parabéns, Você acertou!!")
        break
    elif(maior):
        print("Você errou!!")
        print("O número digitado foi maior que o escolhido!!")
        rodada += 1
    else:
        print("Você errou!")
        print("O número digitado foi menor que o escolhido")
        rodada += 1
print("*"*11)
print("FIM DO JOGO")
print("*"*11)