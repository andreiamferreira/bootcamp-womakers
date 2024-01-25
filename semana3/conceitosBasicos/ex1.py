#Faça um Programa que peça dois números, realize as principais
#operações soma, subtração, multiplicação, divisão

print("CALCULADORA BÁSICA")

action = input('Escolha uma operação: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n')

firstNumer = int(input('Digite o primeiro número: \n'))
secondNumber = int(input('Digite o segundo número: \n'))

match action:
    case "1" | "soma" | "Soma":
         print(f'Resultado de {firstNumer} + {secondNumber} = {firstNumer + secondNumber}')
    case "2" | "subtração" | "subtracao" | "Subtração":
         print(f'Resultado de {firstNumer} - {secondNumber} = {firstNumer - secondNumber}')
    case "3" | "multiplicacao" | "multiplicação" | "Multiplicação":
         print(f'Resultado de {firstNumer} * {secondNumber} = {firstNumer * secondNumber}')
    case "4" | "divisão" | "divisao" | "Divisão":
         print(f'Resultado de {firstNumer}/{secondNumber} = {firstNumer / secondNumber}')



