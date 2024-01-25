# 10. Faça um programa que lê três números inteiros e os mostra em ordem
# crescente

firstNumber, secondNumber, thirdNumber = input('Digite 3 números (separados por espaço): \n').split()

if int(firstNumber) >= int(secondNumber) and int(firstNumber) >= int(thirdNumber):
    if secondNumber >= thirdNumber:
        print(f'{thirdNumber}, {secondNumber}, {firstNumber}')
    else:
        print(f'{secondNumber}, {thirdNumber}, {firstNumber}')
elif int(secondNumber) >= int(firstNumber) and int(secondNumber) >= int(thirdNumber):
    if int(firstNumber) >= int(thirdNumber):
        print(f'{thirdNumber}, {firstNumber}, {secondNumber}')
    else:
        print(f'{firstNumber}, {thirdNumber}, {secondNumber}')
elif int(thirdNumber) >= int(firstNumber) and int(thirdNumber) >= int(secondNumber):
    if firstNumber >= secondNumber:
        print(f'{secondNumber}, {firstNumber}, {thirdNumber}')
    else:
        print(f'{firstNumber}, {secondNumber}, {thirdNumber}')