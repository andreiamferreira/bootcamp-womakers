# Escreva um programa que calcule o tempo de uma viagem. Faça um
# comparativo do mesmo percurso de avião, carro e ônibus.
# Levando em consideração:
# ● avião = 600 km/h
# ● carro = 100 km/h
# ● ônibus = 80 km/h

inputDistance = float(input('Digite a distância a ser percorrida (em km): \n'))

airplaneTime = inputDistance/600
carTime = inputDistance/100
busTime = inputDistance/80

print(f'-----------COMPARAÇÕES DE TEMPO (em horas)------------------\nAvião: {format(airplaneTime, ".2f")}\nCarro: {format(carTime, ".2f")}\nÔnibus: {format(busTime, ".2f")}')