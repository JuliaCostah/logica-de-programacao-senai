import random
lista = []
for i in range(1,11,1):
    lista.append(i)

sorteio = random.choice(lista)
tentativas = 0
while True:
    x = int(input('Tente acertar o número (1 a 10): '))
    tentativas += 1
    if x == sorteio:
        print(f'Parabéns, você acertou! | Tentativas: {tentativas}')
        break
    else:
        print('Você errou! Tente novamente.')