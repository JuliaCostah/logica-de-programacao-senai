import os
numeros = []

while True:
    n = int(input(f'{len(numeros) + 1}° valor (0 para finalizar): '))
    if n == 0:
        break
    else:
        numeros.append(n)
    os.system('cls' if os.name == 'nt' else 'clear')
soma = sum(numeros)
print(f'A soma é {soma}')