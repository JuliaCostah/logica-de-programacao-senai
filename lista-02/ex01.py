numeros = []

for i in range(3):
    numeros.append(float(input(f'{i + 1}° número: ')))
maior = max(numeros)
print(numeros)
print(f'O maior é {maior}')
