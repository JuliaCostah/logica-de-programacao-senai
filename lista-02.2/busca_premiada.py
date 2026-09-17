import os
num = []

for i in range(10):
    n = int(input(f'{i + 1}° número: '))
    num.append(n)
    os.system('cls' if os.name == 'nt' else 'clear')

m = int(input('Qual número buscar? '))
print(num)
if m in num:
    print(f'O {m} foi encontrado {num.count(m)} vezes.')
else:
    print('Número não encontrado.')