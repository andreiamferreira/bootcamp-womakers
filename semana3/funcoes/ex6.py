# 6. Vamos construir um jogo de forca. O programa escolherá
# aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
# secreta será representada por espaços em branco, um para cada letra
# da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
# tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
# na palavra secreta, ela será revelada nas posições correspondentes. Se
# a letra não estiver na palavra, uma mensagem de erro deverá ser
# informada. Após um número máximo de erros, o jogador perde. O jogo
# continua até que o jogador adivinhe a palavra ou exceda o número
# máximo de tentativas.
# Dica: Você precisará importar uma biblioteca para resolver esse
# exercício

from random import choice

def mostrar_letras_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ""
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += "_"
    return palavra_oculta

def jogo_forca():
    tentativas_maximas = 6
    tentativas = 0
    letras_corretas = []
    
    palavras_secretas = [
    "computador",
    "python",
    "aprendizado",
    "desenvolvimento",
    "programar"
    ]

    palavra_escolhida = choice(palavras_secretas)

    print(mostrar_letras_palavra_oculta(palavra_escolhida, letras_corretas))

    while tentativas < tentativas_maximas:
        letra = input("Digite uma letra:\n").lower()

        if letra in letras_corretas:
            print("Você já tentou essa letra. Tente novamente.")

        if letra in palavra_escolhida:
            letras_corretas.append(letra)
            print("Acertou uma letra!")
        else:
            tentativas += 1
            print(f'Errou! Tem mais {tentativas_maximas - tentativas} chance(s)')

        estado_palavra = mostrar_letras_palavra_oculta(palavra_escolhida, letras_corretas)
        print(estado_palavra)

        if "_" not in estado_palavra:
            print("Parabéns! Você adivinhou a palavra.")
            break

    if "_" in estado_palavra:
        print("Você perdeu! A palavra era:", palavra_escolhida)

jogo_forca()
