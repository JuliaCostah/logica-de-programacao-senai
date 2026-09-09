import os
notas = []
aprovados = 0
reprovados = 0
recuperacao = 0

for i in range(5):
    n = float(input(f'{i + 1}° nota (0.0 a 10.0): '))
    notas.append(n)
    if n >= 7.0:
       aprovados += 1
    elif n < 5.0:
        reprovados += 1
    else:
        recuperacao += 1
    os.system('cls' if os.name == 'nt' else 'clear')

media = sum(notas)/len(notas)

print(notas)
print(f'Média: {media:.1f} | Aprovados: {aprovados} | Reprovados: {reprovados} | Recuperação: {recuperacao}')
notas.pop()
print(f'Lista atualizada: {notas}')