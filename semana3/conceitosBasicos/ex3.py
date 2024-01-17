#Faça um Programa que peça a quantidade de quilômetros, transforme
#em metros, centímetros e milímetros.

inputKm = float(input('Digite a quilometragem: '))

meters = inputKm * 1000
cm = inputKm*100000
mm = inputKm*10000000

print(f'\nkm = {inputKm}\nMetros = {meters}\nCentímetros = {cm}\nMilímetros = {mm}')