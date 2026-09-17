def contar_pares (lista):
    pares = 0
    for x in lista:
        if x % 2 == 0:
            pares += 1
    print(f'Quantidade de números pares é {pares}')
    

y = int(input(' quantos números você vai inserir? '))
num = []
for i in range(y):
    n = int(input(f'{i + 1}° número: '))
    num.append(n)

contar_pares(num)