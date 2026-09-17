def contar_pares (lista):
    pares = 0
    for x in lista:
        if x % 2 == 0:
            pares += 1
    return pares

y = int(input('Quantos números você vai inserir? '))
num = []
for i in range(y):
    n = int(input(f'{i + 1}° número: '))
    num.append(n)

resultado = contar_pares(num)
print(f'Quantidade de números pares é {resultado}')