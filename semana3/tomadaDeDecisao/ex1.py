# 1. Faça um Programa que peça dois números e imprima o maior deles.

firstNumber = float(input('Primeiro número: \n'))
secondNumber = float(input('Segundo número: \n'))

if firstNumber > secondNumber:
    print(firstNumber)
elif secondNumber > firstNumber:
    print(secondNumber)
else:
    print(f'Número iguais: {firstNumber}')