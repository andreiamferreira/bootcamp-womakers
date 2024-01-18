# 9. O programa deve calcular e apresentar a quantidade de números pares e
# ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
# informar o valor zero. Certifique-se de incluir validações para garantir que
# apenas números positivos sejam considerados na contagem e cálculos.


userNumberInput = input('Digite um número: \n')
count = 0
evenNumbers = 0
oddNumbers = 0

while (userNumberInput != '0'):
    if userNumberInput > '0':
        if int(userNumberInput) % 2 == 0:
            evenNumbers += 1
        else:
            oddNumbers += 1
    userNumberInput = input('Digite um número: \n')
    
print(f'Quantidade de números pares: {evenNumbers}\nQuantidade de números ímpares: {oddNumbers}')