alcool = float(input('Preço do Álcool: R$'))
gasolina = float(input('Preço da Gasolina: R$'))

proporcao = alcool/gasolina

if proporcao <= 0.70:
    print('Abastecer com álcool pode ser a melhor escolha.') 
else:
    print('Abastecer com gasolina pode ser a melhor escolha.')