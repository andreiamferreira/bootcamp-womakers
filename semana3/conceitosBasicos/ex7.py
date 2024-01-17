# Solicite ao usuário o peso em kg e a altura em metros. Calcule e
# imprima o Índice de Massa Corporal (IMC) usando a fórmula:
# IMC = peso / (altura x altura).

print('------------------CALCULADORA DE IMC----------------')

inputWeight = float(input('Digite o peso (em kg): \n'))
inputHeight = float(input('Digite a altura (em metros): \n'))

imcResult = inputWeight/(inputHeight**2)


print(f'IMC: {format(imcResult, ".2f")}')