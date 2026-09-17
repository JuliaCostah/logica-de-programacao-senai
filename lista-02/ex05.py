import os
notas = []

while True:
    n = float(input('Notas (-1 para finalizar): '))
    if n == -1:
        break
    else:
        notas.append(n)
    os.system('cls' if os.name == 'nt' else 'clear')

if notas:  
    print('Notas Cadastradas')
    for n in notas:
        print(f'{n:.2f} | ',end='')

    media = sum(notas)/len(notas)
    print(f'\nQuantidade: {len(notas)} | Maior nota: {max(notas)} | Menor nota: {min(notas)}')
    notas.sort(reverse=True)
    print(f'Notas em ordem decrescente: {notas}')
else:
    print('Nenhuma nota cadastrada.')
