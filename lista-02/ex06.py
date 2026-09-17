numeros = []
par = []
impar = []
for i in range(6):
    n = int(input(f'{i + 1}° número: '))
    numeros.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(numeros)
print(f'Pares: {len(par)} | Ímpares: {len(impar)}')