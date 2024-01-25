# 5. Crie uma função chamada contar_vogais que recebe uma string
# como parâmetro. Implemente a lógica para contar o número de vogais
# na string e retorne o total de vogais. Solicite ao usuário para inserir uma
# frase e utilize a função para contar as vogais.

inputString = input('Digite uma frase: \n')

def contar_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for letra in inputString:
        if letra in vogais:
            count += 1
    print('Número de vogais na frase: ', count)
            
contar_vogais(inputString)
