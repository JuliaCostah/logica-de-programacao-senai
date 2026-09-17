import os
velocidade = []
ate80 = 0
ate100 = 0
mais100 = 0
for i in range(8):
    v = int(input(f'{i + 1}° velocidade registrada: '))
    velocidade.append(v)
    if v <= 80:
        ate80 += 1
    elif v <= 100:
        ate100 += 1
    else:
        mais100 += 1
    os.system('cls' if os.name == 'nt' else 'clear')

media = sum(velocidade)/len(velocidade)
print(f'Dados:\nFaixa de 80Km/h (Normal): {ate80}\nFaixa de 100Km/h (Infração): {ate100}\nAcima de 100Km/h (Infração grave): {mais100}')
print(f'Média das Velocidades registradas -> {media:.0f}Km/h | Maior velocidade -> {max(velocidade)}Km/h')