import os
positivos = []
negativos = []

for i in range(10):
    n = float(input(f'{i + 1}° valor: '))
    if n < 0:
        negativos.append(n)
    else:
        positivos.append(n)
    os.system('cls' if os.name == 'nt' else 'clear')

print(f'Total de Positivos: {len(positivos)} | Soma: {sum(positivos)}')
print(f'Total de negativos: {len(negativos)} | Vetor -> {negativos}')