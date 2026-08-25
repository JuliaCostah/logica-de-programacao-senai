l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if (l1 == l2 and l2 == l3):
    print('Equilátero.')
elif (l1 != l2 and l2 != l3 and l1 != l3):
    print('Escaleno.')
else:
    print('Isósceles.')
    
