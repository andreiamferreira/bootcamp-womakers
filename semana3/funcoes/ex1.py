# 1. Faça um programa, com uma função que necessite de três
# argumentos, e que forneça a soma desses três argumentos.

def sumNumbers(num1, num2, num3):
    print(num1 + num2 + num3)


numbers = []

print('Digite os 3 números a serem somados: \n')
for i in range(3):
    while True:
        try:
            userNumbers = float(input())
            numbers.append(userNumbers)
            break
        except ValueError:
            print("Número inválido.")

userNum1, userNum2, userNum3 = numbers

sumNumbers(userNum1, userNum2, userNum3)
