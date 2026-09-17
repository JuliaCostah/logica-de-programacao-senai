import os
numeros = []

for i in range(7):
    n = int(input(f'{i + 1}° número: '))
    numeros.append(n)
    os.system('cls' if os.name == 'nt' else 'clear')

m = int(input('Qual número buscar? '))
posicoes = []

for i in range(len(numeros)):
    if numeros[i] == m:
        posicoes.append(i)
if posicoes:
    print(f'{m} encontrado na(s) posição(oẽs) -> {posicoes}')
else:
    print('Valor não encontrado.')