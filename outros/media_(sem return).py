def calcular_media(lista):
    media = sum(lista)/len(lista)
    print(f'A média é {media:.1f}')


num = []
x = int(input('Quantos números você vai inserir? '))
for i in range(x):
    n = int(input(f'Informe o  {i + 1}° número: '))
    num.append((n))

calcular_media(num)