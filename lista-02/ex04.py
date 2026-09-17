numeros = [ 12 , 7 , 9 , 20 , 31 , 44 , 18 , 5 ]
par = []
impar = []
for i in numeros:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
print(f'Pares: {len(par)} | Ímpares: {len(impar)}')