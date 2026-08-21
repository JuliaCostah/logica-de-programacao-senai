num1 = float(input('Informe um número: '))
num2 = float(input('Informe um segundo número: '))

print('Operações:\n\tAdição(+)\n\tSubtração(-)\n\tMultiplicação(*)\n\tDivisão(/)')
operador = input('Escolha uma operação: ')

if operador == '+':
    calculo = num1 + num2
    print(f'A soma é {calculo}')
elif operador == '-':
    calculo = num1 - num2
    print(f'A subtração é {calculo}')
elif operador == '*':
    calculo = num1 * num2
    print(f'A multiplicação é {calculo}')
elif operador == '/':
    if num2 == 0:
        print('ímpossivel dividir por zero.')
    else:    
        calculo = num1/num2
        print(f'A divisão é {calculo}')
else:
    print(f'Operador inválido.') 
    
    