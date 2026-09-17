import random
import os
cadastro = []

for i in range(6):
    nomes = input(f'{i + 1}° nome: ').title()
    cadastro.append(nomes)
    os.system('cls' if os.name == 'nt' else 'clear')
       
print(cadastro)
res = 'S'
while res  == 'S':
    sorteio = random.choice(cadastro)
    print(f'Sorteado(a): {sorteio}')
    print('Outro sorteio? [S/N]')
    res = input().upper().strip()
    os.system('cls' if os.name == 'nt' else 'clear')
print('Encerrando...') 