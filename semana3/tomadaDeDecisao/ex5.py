# 5. Desenvolva um programa que solicite ao usuário os comprimentos dos três
# lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
# equilátero: todos os lados com o mesmo valor
# isósceles: dois lados com o mesmo valor
# escaleno: todos os lados com medidas distintas

sideA, sideB, sideC = input("Digite os 3 lados do triângulo (separe por espaços): ").split()

if sideA == sideB == sideC:
    print('Equilátero')
elif sideA == sideB or sideB == sideC or sideC == sideA:
    print('Isóceles')
else:
    print('Escaleno')