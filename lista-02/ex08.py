import os
numeros = []

for i in range(5):
    n = int(input(f'{i + 1}° número: '))
    numeros.append(n)
    os.system('cls' if os.name == 'nt' else 'clear')

maior = numeros[0]
pos_maior = 0
menor = numeros[0]
pos_menor = 0

for i in range(len(numeros)):
    if numeros[i] > maior:
        maior = numeros[i]
        pos_maior = i
    
    if numeros[i] < menor:
        menor = numeros[i]
        pos_menor = i

print(numeros)
print(f'Maior = {maior} | Posição -> {pos_maior}')
print(f'Menor = {menor} | Posição -> {pos_menor}')