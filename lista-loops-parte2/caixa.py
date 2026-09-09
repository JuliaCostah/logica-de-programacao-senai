saque = []
cont = 0

while cont < 5:
    s = int(input(f'Saque: R$ '))
    if s < 0:
        print('Não aceitamos valores negativos.')
        continue
    else:
        saque.append(s)
    cont += 1

media = sum(saque)/len(saque)
print(saque)
print(f'Saque total: R$ {sum(saque)} | Média: R$ {media:.0f}')
print(f'Saques de R$ 100 -> {saque.count(100)}')
saque.pop()
print(f'Último valor removido:{saque}')