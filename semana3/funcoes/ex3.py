# 3. Escreva um script que pergunta ao usuário se ele deseja converter
# uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
# cada opção, crie uma função.



def celsiusToFahrenheit(temperature):
    convertedTemperature = (temperature*(9/5)) + 32
    print(f'{temperature}ºC convertido para {format(convertedTemperature, ".2f")}ºF')

def fahrenheitToTemperature(temperature):
    convertedTemperature = ((temperature - 32)*(5/9))
    print(f'{temperature}ºF convertido para {format(convertedTemperature, ".2f")}ºC')

def initialMenu(userChoice):
    usersTemperature = float(input('Digite a temperatura a ser convertida: '))
    if usersChoice == '1':
        celsiusToFahrenheit(usersTemperature)
    elif usersChoice == '2':
        fahrenheitToTemperature(usersTemperature)
    else:
        print('Temperatura inválida!')

usersChoice = input('Digite o número referente à opção que deseja:\n1 - Converter de Celsius para Fahrenheit\n2 - Converter de Fahrenheit para Celsius\n')
initialMenu(usersChoice)



