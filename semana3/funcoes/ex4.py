# 4. Crie um programa que leia quanto dinheiro uma pessoa tem na
# carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
# Considere a tabela de conversão abaixo:
# Dólar Americano: R$ 4,91
# Peso Argentino: R$ 0,02
# Dólar Australiano: R$ 3,18
# Dólar Canadense: R$ 3,64
# Franco Suiço: R$ 0,42
# Euro: R$ 5,36
# Libra esterlina: R$ 6,21


def americanDolar(currency):
    convertedValue = currency/4.91
    print(f'Dólar Americano: {format(convertedValue, ".2f")}')
    
def argentinianPeso(currency):
    convertedValue = currency/0.02
    print(f'Peso Argentino: {format(convertedValue, ".2f")}')

def australianDolar(currency):
    convertedValue = currency/3.18
    print(f'Dólar Australiano: {format(convertedValue, ".2f")}')
    
def canadianDolar(currency):
    convertedValue = currency/3.18
    print(f'Dólar Canadense: {format(convertedValue, ".2f")}')

def swissFranc(currency):
    convertedValue = currency/0.42
    print(f'Franco Suíço: {format(convertedValue, ".2f")}')

def euro(currency):
    convertedValue = currency/5.36
    print(f'Euro: {format(convertedValue, ".2f")}')
    
def pounds(currency):
    convertedValue = currency/6.21
    print(f'Libra Esterlina: {format(convertedValue, ".2f")}')
    

def main():
    usersRealAmount = float(input('Digite o valor, em real, a ser convertido:\n'))

    print(f'Com R${usersRealAmount}, você pode comprar os seguintes valores:\n')
    
    americanDolar(usersRealAmount)
    argentinianPeso(usersRealAmount)
    australianDolar(usersRealAmount)
    canadianDolar(usersRealAmount)
    swissFranc(usersRealAmount)
    euro(usersRealAmount)
    pounds(usersRealAmount)

if __name__ == "__main__":
    main()
