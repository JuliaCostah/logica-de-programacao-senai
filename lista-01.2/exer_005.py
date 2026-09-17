print('\tQuadrado  (1)\n\tRetângulo (2)\n\tTriângulo (3)')
figura = input('Escolha a figura: ')

if figura == '1':
    l = float(input('Lado: '))
    area = l**2
    print(f'A área é {area:.2f} m²')
elif figura == '2':
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    area = base * altura
    print(f'A área é {area:.2f} m²')
elif figura == '3':
    base = float(input('Base: '))
    altura = float(input('Altura: '))
    area = base * altura/2
    print(f'A área é {area:.2f} m²')
else:
    print('ERRO! Escolha entre 1,2 ou 3.')