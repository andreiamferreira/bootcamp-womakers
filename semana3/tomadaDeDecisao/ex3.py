# 3. Faça um programa que peça uma nota, entre zero e dez. Mostre uma
# mensagem caso o valor seja inválido e continue pedindo até que o usuário
# informe um valor válido.

inputgrade = float(input('Digite uma nota entre 0 e 10: '))

while (inputgrade > 10):
    print('Valor inválido')
    inputgrade = float(input('Digite uma nota: '))
