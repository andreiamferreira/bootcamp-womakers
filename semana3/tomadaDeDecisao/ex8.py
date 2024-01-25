# 8. Criar um programa em Python que solicite três números ao usuário, utilize
# estruturas condicionais para determinar o maior entre eles e apresente o
# resultado.

firstNumber, secondNumber, thirdNumber = input('Digite 3 números (separados por espaço): \n').split()

if (firstNumber > secondNumber and firstNumber > secondNumber):
    print('Maior número: ' + firstNumber)
elif (secondNumber > firstNumber and secondNumber > thirdNumber):
    print('Maior número: ' + secondNumber)
elif (thirdNumber > firstNumber and thirdNumber > secondNumber):
    print('Maior número: ' + thirdNumber)
else:
    print('Números iguais!')
    

