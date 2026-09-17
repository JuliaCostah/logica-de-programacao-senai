def calcular_media(lista):

    media = sum(lista)/len(lista)
    
    return media

list = []
x = int(input('Quantos números você vai inserir? '))
for i in range(x):
    n = int(input(f'Informe o  {i + 1}° número: '))
    list.append((n))

res = calcular_media(list)
print(f'A média é {res:.1f}')