#Receba do usuário a quantidade de litros de combustível consumidos e
#a distância percorrida. Calcule e imprima o consumo médio em km/l.

inputLiters = float(input('Digite a quantidade de litros de combustível consumidos: \n'))
inpuitDistance = float(input('Digite a distância percorrida: \n'))

avgResult = inpuitDistance/inputLiters

print(f'O consumo médio foi de {format(avgResult, ".2f")}km/L')

