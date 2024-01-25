# 2. Reverso do número. Faça uma função que retorne o reverso de um
# número inteiro informado. Por exemplo: 127 -> 721

def reverseNumber(number):
    try:
        reversedNumber = str(number)[::-1]
        print(reversedNumber)
    except ValueError: 
        print('Número inválido!')
        
userNumber = int(input('Digite um número inteiro a ser invertido: \n'))
reverseNumber(userNumber)